function waterMeter(){
    var waterSwitch = document.getElementById('water-switch');
    var waterMeter1 = document.getElementById('inner-water-meter')
    var waterMeter2 = document.getElementById('inner-water-meter2')

    if (waterSwitch.checked){
        waterMeter1.style.height = "400px";   
        waterMeter2.style.height = "300px"  
    }
    else if (waterSwitch.checked == false) {
        waterMeter1.style.height = "0px";
        waterMeter2.style.height = "0px";   
    }
}

function lightMeter(){
    var lightSwitch = document.getElementById('light-switch');
    var lightMeter = document.getElementById('light-meter')

    if (lightSwitch.checked){
        lightMeter.style.background = "yellow";       
    }
    else if (lightSwitch.checked == false) {
        lightMeter.style.background = "grey";   
    }
}
