function checkColors() {
    const preferredColors = 'input[name="preferred"]:checked';
    const selectedPreferredColors = document.querySelectorAll(preferredColors);
    const preferredColorsCnt = selectedPreferredColors.length;

    const dislikedColors = 'input[name="disliked"]:checked';
    const selectedDislikedColors = document.querySelectorAll(dislikedColors);
    const dislikedColorsCnt = selectedDislikedColors.length;

    //alert(preferredColorsCnt + ',' + dislikedColorsCnt);

    //좋아하는 색상 3개 + 안좋아하는 색상 1개 선택 경우
    while((preferredColorsCnt == 3) && (dislikedColorsCnt == 1)) {
        //선택한 색상 -> JSON
        var colorsArray = new Array();
        var arrayCount = 0;

        for(i=0; i < selectColors.preferred.length; i++){
            if(selectColors.preferred[i].checked) {
                colorsArray[arrayCount] = selectColors.preferred[i].value;
                arrayCount ++;
            }
        }

        for(i=0; i < selectColors.disliked.length; i++){
            if(selectColors.disliked[i].checked) {
                //colorsArray[arrayCount] = selectColors.disliked[i].value;
                //arrayCount ++;
                //alert(selectColors.disliked[i].value);
                document.getElementById("disliked_color").value = selectColors.disliked[i].value;
            }
        }

        var colorsJson = JSON.stringify(colorsArray);
        document.getElementById("liked_colors").value = colorsArray;
        //alert(colorsArray);

        return true;
    }


    if(preferredColorsCnt == 0) {
        alert("마음에 드는 색상을 선택해주세요.");
        return false;
    }
    else if(preferredColorsCnt == 1) {
        alert("마음에 드는 색상을 2개 더 선택해주세요.");
        return false;
    }
    else if(preferredColorsCnt == 2) {
        alert("마음에 드는 색상을 1개 더 선택해주세요.");
        return false;
    }
    else if(preferredColorsCnt > 3) {
        alert("마음에 드는 색상은 3개까지 선택할 수 있어요.");
        return false;
    }

    if(dislikedColorsCnt == 0) {
        alert("마음에 들지 않는 색상을 선택해주세요.");
        return false;
    }
    else if(preferredColorsCnt > 1) {
        alert("마음에 들지 않는 색상은 1개까지 선택할 수 있어요.");
        return false;
    }

    
}