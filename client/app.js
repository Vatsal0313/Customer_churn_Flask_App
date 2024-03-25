function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i in uiBathrooms) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1;
}
function getseniorcitizenValue() {
    var uiBHK = document.getElementsByName("uiseniorcitizen");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function getpartnerValue() {
    var uiBHK = document.getElementsByName("uipartner");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function getdependentsValue() {
    var uiBHK = document.getElementsByName("uidependents");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function gettenureValue() {
    var uiBHK = document.getElementsByName("uitenure");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function getphoneserviceValue() {
    var uiBHK = document.getElementsByName("uiphoneservice");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function getmultiplelinesValue() {
    var uiBHK = document.getElementsByName("uimultiplelines");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function getonlinesecurityValue() {
    var uiBHK = document.getElementsByName("uionlinesecurity");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function getonlinebackupValue() {
    var uiBHK = document.getElementsByName("uionlinebackup");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function getdeviceprotectionValue() {
    var uiBHK = document.getElementsByName("uideviceprotection");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function gettechsupportValue() {
    var uiBHK = document.getElementsByName("uitechsupport");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function getstreamingtvValue() {
    var uiBHK = document.getElementsByName("uistreamingtv");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function getstreamingmoviesValue() {
    var uiBHK = document.getElementsByName("uistreamingmovies");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}
function getpaperlessbillingValue() {
    var uiBHK = document.getElementsByName("uipaperlessbilling");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}

function onClickedCustomerChurn() {
    console.log("Customer Churn Button Clicked")
    var gender = document.getElementById("uigender")
    var seniorcitizen = getseniorcitizenValue()
    var partner = getpartnerValue()
    var dependents = getdependentsValue()
    var tenure = document.getElementById("uitenure")
    var phoneservice = getphoneserviceValue()
    var multiplelines = getmultiplelinesValue()
    var onlinesecurity = getonlinesecurityValue()
    var onlinebackup = getonlinebackupValue()
    var deviceprotection = getdeviceprotectionValue()
    var techsupport = gettechsupportValue()
    var streamingtv = getstreamingtvValue()
    var streamingmovies = getstreamingmoviesValue()
    var paperlessbilling = getpaperlessbillingValue()
    var monthlycharges = document.getElementById("uimonthlycharges")
    var totalcharges = document.getElementById("uitotalcharges")
    var internetservice = document.getElementById("uiinternetservice");
    var contract = document.getElementById("uicontract")
    var paymentmethod = document.getElementById("uipaymentmethod");
    var estPrice = document.getElementById("uiEstimatedPrice")

    var url = "http://127.0.0.1:5000/predict_customer_churn";

    $.post(url, {
        // bath: bathrooms,
        gender: gender.value,
        seniorcitizen: seniorcitizen,
        partner: partner,
        dependents: dependents,
        tenure: parseInt(tenure.value),
        phoneservice: phoneservice,
        multiplelines: multiplelines,
        onlinesecurity: onlinesecurity,
        onlinebackup: onlinebackup,
        deviceprotection: deviceprotection,
        techsupport: techsupport,
        streamingtv: streamingtv,
        streamingmovies: streamingmovies,
        paperlessbilling: paperlessbilling,
        monthlycharges: parseFloat(monthlycharges.value),
        totalcharges: parseFloat(totalcharges.value),
        internetservice: internetservice.value,
        paymentmethod: paymentmethod.value,
        contract: contract.value
    }, function (data, status) {
        console.log(data.estimated_price);
        if(data.estimated_price==0){
            data.estimated_price="NO"
        }
        else
        {
            data.estimated_price="YES"
        }
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "</h2>";
        console.log(status);
    });
}

function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_paymentmethod_types"; 
    var url2 = "http://127.0.0.1:5000/get_contract_types"; 
    var url3 = "http://127.0.0.1:5000/get_internetservice_types"; 
    $.get(url, function (data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var paymentmethod = data.paymentmethod;
            var uipaymentmethod = document.getElementById("uipaymentmethod");
            $('#uipaymentmethod').empty();
            paymentmethod_types = paymentmethod
            for (var i in paymentmethod_types) {
                var opt = new Option(paymentmethod_types[i]);
                $('#uipaymentmethod').append(opt);
            }
        }
    });
    $.get(url2, function (data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var contract = data.contract;
            var uicontract = document.getElementById("uicontract");
            $('#uicontract').empty();
            contract_types = contract
            for (var i in contract_types) {
                var opt = new Option(contract_types[i]);
                $('#uicontract').append(opt);
            }
        }
    });
    $.get(url3, function (data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var internetservice = data.internetservices;
            var uiinternetservice = document.getElementById("uiinternetservice");
            $('#uiinternetservice').empty();
            internetservice_types = internetservice
            for (var i in internetservice_types) {
                var opt = new Option(internetservice_types[i]);
                $('#uiinternetservice').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;