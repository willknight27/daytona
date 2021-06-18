const cargarApi = async function(){

    let res = await axios.get("https://mindicador.cl/api/");
    //console.log(res);

    //Valor Indicadores
    let valor_uf = res.data.uf.valor;
    let valor_dolar = res.data.dolar.valor;
    let valor_utm = res.data.utm.valor;

    document.querySelector("#valor-uf").innerText = valor_uf;
    document.querySelector("#valor-dolar").innerText = valor_dolar;
    document.querySelector("#valor-utm").innerText = valor_utm;
}


document.addEventListener("DOMContentLoaded", ()=>{
    cargarApi();
});