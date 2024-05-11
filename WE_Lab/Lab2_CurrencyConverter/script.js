function ConvertDollarAndPKR(givenAmount, fromCurrency) {
    if (fromCurrency === "Dollar") {
        return (givenAmount * 176.25)
    }
    return (givenAmount / 176.25);
}

function ConvertDollarAndEuro(givenAmount, fromCurrency) {
    if (fromCurrency === "Dollar") {
        return (givenAmount / 0.88)
    }
    return (givenAmount * 0.88);
}

function ConvertPKRAndEuro(givenAmount, fromCurrency) {
    if (fromCurrency === "PKR") {
        return (givenAmount / 199.77)
    }
    return (givenAmount * 199.77);
}

function generatePrimeNumbers(primeNo, amount) {
    var primes = [];
    var i = 0;
    for (i = 2; i <= amount; i++) {
        if (i == 2 || i == 3) {
            primes.push(i);
        }
        else if (i % 2 != 0 && i % 3 != 0) {
            primes.push(i);
        }
    }
    var primeStr = "";
    for (i = 0; i < primes.length; i++) {
        if (i === primes.length - 1) {
            primeStr += `<span id=p-${i + 1}>${primes[i]}</span>`;
        }
        else {
            primeStr += `<span id=p-${i + 1}>${primes[i]}, </span>`;
        }
    }
    primeNo.innerHTML = primeStr;
}

function generateEvenNumbers(evenNo, amount) {
    var even = [];
    var i = 0;
    for (i = 2; i <= amount; i++) {
        if (i == 2 || i % 2 == 0) {
            even.push(i);
        }
    }
    var evenStr = "";
    for (i = 0; i < even.length; i++) {
        if (i === even.length - 1) {
            evenStr += `<span id=e-${i + 1}>${even[i]}</span>`;
        }
        else {
            evenStr += `<span id=e-${i + 1}>${even[i]}, </span>`;
        }
    }
    evenNo.innerHTML = evenStr;
}

function handleCurrencyConverter() {
    var fromCurrency = document.getElementById("fromCurrency").value;
    var toCurrency = document.getElementById("toCurrency").value;
    var givenAmount = document.getElementById("Amount").value;
    var outputResult = document.getElementById("output");
    var resultAmount = 0.0;
    if (fromCurrency !== "" && toCurrency !== "") {
        (fromCurrency === "Dollar" && toCurrency === "PKR") || (fromCurrency === "PKR" && toCurrency === "Dollar")
            ? resultAmount = ConvertDollarAndPKR(givenAmount, fromCurrency)
            : (fromCurrency === "Dollar" && toCurrency === "Euro") || (fromCurrency === "Euro" && toCurrency === "Dollar")
                ? resultAmount = ConvertDollarAndEuro(givenAmount, fromCurrency)
                : (fromCurrency === "PKR" && toCurrency === "Euro") || (fromCurrency === "Euro" && toCurrency === "PKR")
                    ? resultAmount = ConvertPKRAndEuro(givenAmount, fromCurrency)
                    : null
    }
    outputResult.value = parseInt(resultAmount);
    var primeText = document.getElementById("primeText").innerText = "Prime Numbers upto this amount:";
    var primeNo = document.getElementById("primeNo");
    var evenText = document.getElementById("evenText").innerText = "Even Numbers upto this amount:";
    var evenNo = document.getElementById("evenNo");
    generatePrimeNumbers(primeNo, parseInt(resultAmount));
    generateEvenNumbers(evenNo, parseInt(resultAmount));

    var indexPrime = document.getElementById("indexprime");
    var indexEven = document.getElementById("indexeven");
    var indexMatcher = document.getElementById("indexMatcher");

    var primeIndex = 0, evenIndex = 0;
    primeNo.addEventListener("mouseover", (event) => {
        var strings = event.target.id;
        primeIndex = parseInt(strings.slice(2, strings.length));

        indexPrime.innerHTML = `Index of Prime Number = <span>${primeIndex}</span>`
        if (primeIndex != 0 && evenIndex != 0) {
            primeIndex > evenIndex ? indexMatcher.innerText = `Index of Prime Number is "greater then" Index of Even Number`
                : primeIndex < evenIndex ? indexMatcher.innerText = `Index of Prime Number is "less then" Index of Even Number`
                    : indexMatcher.innerText = `Index of Prime Number is "equal to" Index of Even Number`
        }
    })

    evenNo.addEventListener("mouseover", (event) => {
        var strings = event.target.id;
        evenIndex = parseInt(strings.slice(2, strings.length));

        indexEven.innerHTML = `Index of Even Number = <span>${evenIndex}</span>`
        if (primeIndex != 0 && evenIndex != 0) {
            primeIndex > evenIndex ? indexMatcher.innerText = `Index of Prime Number is "greater then" Index of Even Number`
                : primeIndex < evenIndex ? indexMatcher.innerText = `Index of Prime Number is "less then" Index of Even Number`
                    : indexMatcher.innerText = `Index of Prime Number is "equal to" Index of Even Number`
        }
    })


}