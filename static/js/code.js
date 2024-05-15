function calculate_IMC() {
    let weightValue = document.querySelector('.Weight').value;
    let heightValue = document.querySelector('.Height').value;
    let informazioni = {
        weight: weightValue,
        height: heightValue
    }
    fetch('https://hujun017-input-t2cub3ucm72.ws-eu111.gitpod.io/imc_fetch', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(informazioni),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
    })
    .catch((error) => {
        console.error('Errore nella richiesta fetch:', error);
    })
}