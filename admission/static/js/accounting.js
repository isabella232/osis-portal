$('document').ready(function(){
    // for secondary_education and diplomas screen
    if ($('#form_accounting')){

        $('#pnl_study_grant_number').css('visibility', 'hidden').css('display','none');
        $('#pnl_no_study_grant').css('visibility', 'hidden').css('display','none');
        $('#pnl_study_grant_detail').css('visibility', 'hidden').css('display','none');
        $('#pnl_scholarship_organization').css('visibility', 'hidden').css('display','none');

        if ($("input[name='study_grant']:checked").val()=='true'){
            $('#pnl_study_grant_number').css('visibility', 'visible').css('display','block');
            $('#pnl_study_grant_detail').css('visibility', 'visible').css('display','block');
        }
        if ($("input[name='study_grant']:checked").val()=='false'){
            $('#pnl_no_study_grant').css('visibility', 'visible').css('display','block');
            $('#pnl_study_grant_detail').css('visibility', 'visible').css('display','block');
        }
        if ($("input[name='scholarship']:checked").val()=='true'){
            $('#pnl_scholarship_organization').css('visibility', 'visible').css('display','block');
        }

    }
});

