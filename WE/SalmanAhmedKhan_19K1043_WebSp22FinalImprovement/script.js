function calculate()
{
    let firstValue = parseInt(document.getElementById("firstNumber").value);

    let secondValue =  parseInt(document.getElementById("secondNumber").value);

    let operator =  (document.getElementById("select").value);

    let result = null;
    switch(operator)
    {
        case '+':
            result = firstValue + secondValue;
            break;
        case '-':
            result = firstValue - secondValue;
            break;
        case '*':
            result = firstValue * secondValue;
            break;
        case '/':
            result = (firstValue / secondValue).toFixed(1);
            break;
    }
    let s = document.createElement('span');
    s.setAttribute('id', 'result');
    s.innerText = result;
    let d = document.getElementById("form");
    d.appendChild(s);
}