function calculate_IMC() {
    let weight = document.gte
    let informazioni = {
        weight: ,
        height:
    }
    fetch('https://hujun017-input-t2cub3ucm72.ws-eu111.gitpod.io/imc_fetch', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({richiesta: informazioni}),
    })
}