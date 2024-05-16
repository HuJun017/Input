function calculate_IMC() {
    let weightValue = document.getElementById('Weight').value;
    let heightValue = document.getElementById('Height').value
    let informazioni = {
        weight: weightValue,
        height: heightValue
    }
    console.log(informazioni);
    fetch('https://3245-hujun017-input-t2cub3ucm72.ws-eu111.gitpod.io/imc_fetch', {
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
}