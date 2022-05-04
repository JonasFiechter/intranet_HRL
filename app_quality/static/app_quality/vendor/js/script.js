'use strict'

let btn_radio = document.querySelectorAll('.yes-no');
const btn = document.querySelector('.btn1');
const patient_forms = document.querySelectorAll('.patient-form');


if (btn_radio) {
    btn_radio.forEach((item) => {
        item.addEventListener('change', function(event) {
            var item = event.target.value;
            if (item === 'yes') {
                for (const i of patient_forms) {
                    i.classList.remove('hidden');
                    }
                } else if (item === 'no') {
                    for (const i of patient_forms) {
                        i.classList.add('hidden')
                    }          
            }
        })
    })
}
