let btn = document.getElementById("convert_btn");

function convert() {
   
    let toUnit = document.getElementById("toUnit").value;
    let fromUnit = document.getElementById("fromUnit").value;
    let temperature = parseFloat(document.getElementById("temperature").value);

    
    let convert_value;
    let result_Unit;

    switch (fromUnit) {
        case "Celsius":
            if (toUnit === "Fahrenheit") {
                convert_value = (temperature * (9 / 5)) + 32;
                result_Unit = "Fahrenheit";
            } else if (toUnit === "Kelvin") {
                convert_value = temperature + 273.15;
                result_Unit = "Kelvin";
            } else {
                convert_value = temperature;
                result_Unit = "Celsius";
            }
            break;

        case "Fahrenheit":
            if (toUnit === "Celsius") {
                convert_value = (temperature - 32) * (5 / 9);
                result_Unit = "Celsius";
            } else if (toUnit === "Kelvin") {
                convert_value = (temperature - 32) * (5 / 9) + 273.15;
                result_Unit = "Kelvin";
            } else {
                convert_value = temperature;
                result_Unit = "Fahrenheit";
            }
            break;

        case "Kelvin":
            if (toUnit === "Celsius") {
                convert_value = temperature - 273.15;
                result_Unit = "Celsius";
            } else if (toUnit === "Fahrenheit") {
                convert_value = (temperature - 273.15) * 1.8 + 32;
                result_Unit = "Fahrenheit";
            } else {
                convert_value = temperature;
                result_Unit = "Kelvin";
            }
            break;
    }

    document.getElementById("result").value = convert_value.toFixed(2);
    document.getElementById("result").setAttribute('placeholder', result_Unit); // Show unit in placeholder
}


btn.addEventListener("click", convert);
