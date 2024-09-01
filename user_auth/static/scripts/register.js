document.addEventListener('DOMContentLoaded', (event) => {
  const steps = document.querySelectorAll('.step');
  const sliderProgress = document.getElementById('sliderProgress');
  const formSteps = document.querySelectorAll('.form-step');
  const backHomeBtn = document.querySelector('.back-home');
  const nextBtn = document.querySelector('.next');
  const prevBtn = document.querySelector('.previous');
  const submitBtn = document.querySelector('.submit-btn');
  const form = document.getElementById('registerForm'); // Target the form element
  let currentStep = parseInt(localStorage.getItem('currentStep')) || 1;

  function validateStep() {
    let valid = true;
    const currentFormStep = formSteps[currentStep - 1];
    const inputs = currentFormStep.querySelectorAll('input, select, textarea');

    // Clear previous errors
    currentFormStep.querySelectorAll('.error-message').forEach(msg => msg.textContent = '');

    inputs.forEach(input => {
      if (input.required && !input.value.trim()) {
        const errorMsg = document.getElementById(`${input.id}Error`);
        if (errorMsg) {
          errorMsg.textContent = 'This field is required';
        }
        valid = false;
      }

      // Additional validation for password confirmation
      if (input.id === 'confirmPassword') {
        const password = document.getElementById('password').value;
        if (input.value !== password) {
          const errorMsg = document.getElementById(`${input.id}Error`);
          if (errorMsg) {
            errorMsg.textContent = 'Passwords do not match';
          }
          valid = false;
        }
      }
    });

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username && password && username === password) {
      document.getElementById('usernameError').innerText = "Username and password cannot be the same";
      document.getElementById('passwordError').innerText = "Username and password cannot be the same";
      valid = false;
    }
    return valid;
  }

  function updateSlider() {
    const progressPercent = (currentStep / formSteps.length) * 100;
    sliderProgress.style.width = `${progressPercent}%`;

    steps.forEach((step, index) => {
      if (index < currentStep) {
        step.classList.add('active');
      } else {
        step.classList.remove('active');
      }
    });

    formSteps.forEach((formStep, index) => {
      formStep.style.display = index === currentStep - 1 ? 'block' : 'none';
    });

    if (currentStep === formSteps.length) {
      nextBtn.style.display = 'none';
      submitBtn.style.display = 'block';
    } else {
      nextBtn.style.display = 'block';
      submitBtn.style.display = 'none';
    }

    if (currentStep === 1) {
      prevBtn.disabled = true;
      prevBtn.style.display = "none";
      backHomeBtn.style.display = 'block';
    } else {
      prevBtn.disabled = false;
      prevBtn.style.display = "block";
      backHomeBtn.style.display = 'none';
    }
  }

  function saveDataToLocalStorage() {
    const formData = {};
    document.querySelectorAll('input, select, textarea').forEach(input => {
      formData[input.name] = input.value;
    });
    localStorage.setItem('formData', JSON.stringify(formData));
  }

  function loadDataFromLocalStorage() {
    const formData = JSON.parse(localStorage.getItem('formData')) || {};
    document.querySelectorAll('input, select, textarea').forEach(input => {
      if (formData[input.name]) {
        input.value = formData[input.name];
      }
    });
  }

  function clearLocalStorage() {
    localStorage.removeItem('formData');
    localStorage.removeItem('currentStep');
  }
  
  function clearCurrentStep() {
    const currentFormStep = formSteps[currentStep - 1];
    const inputs = currentFormStep.querySelectorAll('input, select, textarea');

    inputs.forEach(input => {
      input.value = '';
    });

    // Also update the localStorage to reflect the cleared data
    saveDataToLocalStorage();
  }

  // Add event listeners to all clear buttons
  document.querySelector('.clear-btn').addEventListener('click', () => {
    clearCurrentStep(); // Clear data for the current step only
  });

  nextBtn.addEventListener('click', () => {
    if (validateStep()) {
      saveDataToLocalStorage();
      if (currentStep < formSteps.length) {
        currentStep++;
        localStorage.setItem('currentStep', currentStep);
        updateSlider();
      }
    }
  });

  prevBtn.addEventListener('click', () => {
    if (currentStep > 1) {
      currentStep--;
      localStorage.setItem('currentStep', currentStep);
      updateSlider();
    }
  });

  form.addEventListener('submit', (event) => {
    if (!validateStep()) {
      event.preventDefault(); // Prevent form submission if validation fails
      return;
    }
    clearLocalStorage();
  });

  loadDataFromLocalStorage();
  updateSlider();
});

function show() {
  const x = document.getElementById("password");
  const y = document.getElementById("confirmPassword");
  if (x.type === "password") {
    x.type = "text";
    y.type = "text";
  } else {
    x.type = "password";
    y.type = "password";
  }
}