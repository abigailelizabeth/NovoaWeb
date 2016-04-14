$(document).ready(function () {
var size = 5;
$('#reset').click(function(){
    for(var i=1; i < size; i++){
        $('#sel'+i).val('None');
    }
    $('#cost').text('0');
});

$('#compute').click(function(){
    var code="";
    var repeated = false,
        noselect = false;
    for(var i =1; i < size; i++){
        if($('#sel' + i).val() == null){
            noselect=true;
            i = size; j = size;
        }
        for(var j = i+ 1; j<size; j++){
            if($('#sel' + j).val() == null){
                noselect=true;
                i=size; j=size;
            }
           if($('#sel' + i).val() == $('#sel'+ j).val()){
                repeated = true;
               i=size; j=size;
            }

        }
        code=code+ $('#sel' + i).val();

    }
    if(repeated == true){alert('One department per location please')}
    else if(noselect == true){alert('Select a department for all locations')}
    else{
        alert(code);
    }
});
});