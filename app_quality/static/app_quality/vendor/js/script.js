'use strict'

let btn_radio = document.querySelectorAll('input[name="with-patient-option"]');
console.log(btn_radio)
const patient_fields_radio = function() {
    console.log('clicked')
}

if (btn_radio) {
    btn_radio.forEach((item) => {
        item.addEventListener('change', function(event) {
            var item = event.target.value;
            console.log(item)
            console.log('working')
        })
    })
}
