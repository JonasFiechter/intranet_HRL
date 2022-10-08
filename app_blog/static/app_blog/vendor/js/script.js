'use strict'

console.log('works');

function confirm_btn(message) {
    if (confirm(message)) {
        return
    } else {
        window.location.replace('#')
    }
}

function check_delete(post_title, url) {
    if (confirm(`Confirmar remoção do post: \n${post_title}`)) {
        window.location.replace(url)
    }
}

let btn_radio = document.querySelectorAll('.yes-no');
const patient_forms = document.querySelectorAll('.patient-form');

let btn_radio_drug = document.querySelectorAll('.yes-no-drug');
const drug_forms = document.querySelectorAll('.drug-form');


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

if (btn_radio_drug) {
    btn_radio_drug.forEach((item) => {
        item.addEventListener('change', function(event) {
            var item = event.target.value;
            if (item === 'yes') {
                for (const i of drug_forms) {
                    i.classList.remove('hidden');
                    }
                } else if (item === 'no') {
                    for (const i of drug_forms) {
                        i.classList.add('hidden')
                }          
            }
        })
    })
}

