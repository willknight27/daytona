function iniciarMap(){
    var coord = {lat: -33.016841,lng:-71.550321};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 15,
        center: coord
    });

    //crear marcador en mapa
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}