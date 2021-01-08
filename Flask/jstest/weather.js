const COORDS = 'coords';

function saveCoords(coordsObj){
    localStorage.setItem(COORDS, JSON.stringify(coordsObj));
}

function handleGeoSucces(position){
    const latitue = position.coords.latitue;
    const longitude = position.coords.longitude;
    const coordsObj = {
        latitue: latitue,
        longitude: longitude
    };
    saveCoords(coordsObj);
}

function handleError(){
    console.log('Cant access geo location')
}

function askForcoords(){
    navigator.geolocation.getCurrentPosition(handleGeoSucces, handleError);
}

function loadCoords(){
    const loadedCoords = localStorage.getItem(COORDS);
    if(loadedCoords ===null){
        askForcoords();
    }else{

    }
}

function init(){
    loadCoords();
}

init();