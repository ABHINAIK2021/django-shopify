$(document).ready(function () {
    $('.table').DataTable();
});

const purchasesOnchange = () => {
    let purchasesQty = parseInt(document.getElementById('purchasesQty').value);
    let purchasesRate = parseInt(document.getElementById('purchasesRate').value);
    let purchasesAmount = purchasesQty * purchasesRate;
    document.getElementById('purchasesAmount').value = parseFloat(purchasesAmount).toFixed(2);
    let purchasesDiscountPercentage = parseInt(document.getElementById('purchasesDiscountPercentage').value);
    let purchasesDiscountAmount = (purchasesAmount / 100) * purchasesDiscountPercentage;
    document.getElementById('purchasesDiscountAmount').value = parseFloat(purchasesDiscountAmount).toFixed(2);
    let purchasesNetAmount = purchasesAmount - purchasesDiscountAmount;
    document.getElementById('purchasesNetAmount').value = parseFloat(purchasesNetAmount).toFixed(2);
    let purchasesGSTPercentage = parseInt(document.getElementById('purchasesGSTPercentage').value);
    let purchasesGSTAmount = (purchasesNetAmount / 100) * purchasesGSTPercentage;
    document.getElementById('purchasesGSTAmount').value = parseFloat(purchasesGSTAmount).toFixed(2);
    let purchasesGrossAmount = purchasesNetAmount + purchasesGSTAmount;
    document.getElementById('purchasesGrossAmount').value = parseFloat(purchasesGrossAmount).toFixed(2);
}

const salesOnchange = () => {
    let salesQty = parseInt(document.getElementById('salesQty').value);
    let salesRate = parseInt(document.getElementById('salesRate').value);
    let salesAmount = salesQty * salesRate;
    document.getElementById('salesAmount').value = parseFloat(salesAmount).toFixed(2);
    let salesDiscountPercentage = parseInt(document.getElementById('salesDiscountPercentage').value);
    let salesDiscountAmount = (salesAmount / 100) * salesDiscountPercentage;
    document.getElementById('salesDiscountAmount').value = parseFloat(salesDiscountAmount).toFixed(2);
    let salesNetAmount = salesAmount - salesDiscountAmount;
    document.getElementById('salesNetAmount').value = parseFloat(salesNetAmount).toFixed(2);
    let salesGSTPercentage = parseInt(document.getElementById('salesGSTPercentage').value);
    let salesGSTAmount = (salesNetAmount / 100) * salesGSTPercentage;
    document.getElementById('salesGSTAmount').value = parseFloat(salesGSTAmount).toFixed(2);
    let salesGrossAmount = salesNetAmount + salesGSTAmount;
    document.getElementById('salesGrossAmount').value = parseFloat(salesGrossAmount).toFixed(2);
}
