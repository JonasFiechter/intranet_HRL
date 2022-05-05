'use strict'

console.log('works')

function check_delete(post_title) {
    console.log('function working')
    return confirm(`Confirmar remoção do post: \n${post_title}`)
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

