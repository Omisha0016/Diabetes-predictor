$('button').click(function(){
    var s2 = $('input').val();
    window.open(`https://www.practo.com/search?results_type=doctor&q=%5B%7B%22word%22%3A%22diabetes%20doctor%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22common_name%22%7D%5D&city=${s2}`);
    return false;
});