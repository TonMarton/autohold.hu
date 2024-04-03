/*
extension of the jfu:
-----------------
 - everything is defined here, which alters the behaviour of the jfu and django admin change_form,
apart from a small part in jfu files...
-----------------
handle the dictionaries of images, pass them to the form, for server data
load the existing images to the ui
implement arrow clicks to shuffle the rows around (visual reprresentation of the order of pictures to be displayed on the server)
and others...
*/

$(document).ready(function() {

    getCarIdsAndNames();
    $('.fileinput-button').find('span').text('Új Képek');
    $('.fileupload-buttonbar').find('button').hide();

    var uploadsFinished = 0;
    var numberOfUploads;
    var $form = $('#fileupload');
    var oldData = $('#id_image_locations').val();
    if (oldData) {
        var jsonOldData = JSON.parse(oldData);
    }

    // here we load in the existing files
    $form.fileupload('option', 'done').call($form, $.Event('done'), {result: {files: jsonOldData}});

    // listener bound to done
    $form.bind('fileuploadcompleted', function (e, data) {
        var jsonNewData = data;
        if (data['_response']) {
            newFiles = data['_response']['result']['files'];

            oldData = $('#id_image_locations').val();
            if (oldData){
                jsonOldData = JSON.parse(oldData);
            }

            //if there are images already
            if (oldData && oldData !== []) {
                updatedData = savePosition(newFiles);
                $('#id_image_locations').val(JSON.stringify(updatedData));
            } else {
                $('#id_image_locations').val(JSON.stringify(newFiles));
            }
            uploadsFinished = uploadReady(uploadsFinished, numberOfUploads);
        }
    });

    //listeners for the existing files
    setInitialButtonListeners();

    //set listeners on adding a new file, add class 'inited' to keep track of older ones
    $('#fileupload').bind('fileuploadadded', function (e, data) {
        $('.table-striped').find('.start').hide();
        var newRows = $('.template-upload:not(.inited)');
        $(newRows).each( function() {
            $(this).addClass('inited');
            setButtonClickListeners($(this).children('.shuffle_cell'));
        });
    });

    //set listeners to alter the image_locations (modified jquery.fileupload-ui.js _deleteHandler method to receive the data)
    $('#fileupload').bind('fileuploaddestroy', function (e, data) {
        parsedLocations = JSON.parse($('#id_image_locations').val());
        $(parsedLocations).each(function(index) {
            if (this['name'] == data['fileName'] ) {
                parsedLocations.splice(index, 1);
                $('#id_image_locations').val(JSON.stringify(parsedLocations));
            }
        });
    });

    //
    $( "input[name^='_save']" ).click(function( event ) {
        if( $('#id_név').val() === '') {
            window.location.href = "#id_név";
            alert('A név mezőt kötelező kitölteni!');
            return false;
        }
        event.preventDefault();
        numberOfUploads = $('.table-striped').find('tr').filter('.template-upload').length;
        if (numberOfUploads > 0) {
            startLoadingUI();
            $('.table-striped').find('.start').click();
        } else {
            submitFinal();
        }
    });
});

function startLoadingUI() {
    //scroll to main progressbar
    $(document).scrollTop( $(".fileupload-progress").offset().top);
    //disable scrolling
    $('html, body').css({overflow: 'hidden',height: '100%'});
    //place div above all other elements, to prevent any user interactions
    $('body').append("<div id='loadWrapper' style='background-color: rgba(82, 87, 99, 0.35);z-index: 998;position: absolute;left: 0;top: 0;width: 100%;height: 100%;'></div>");
    $('body').append("<div id='loadWrapperContainer' style='background-color: rgba(0, 0, 0, 0);z-index: 998;position: absolute;left: 0; top: 60%;width: 100%;height: 100px;'></div>");
    $('#loadWrapperContainer').append("<div id='loadPrompt' style='margin-left: auto; margin-right: auto;padding-top: 10px; padding-bottom: 10px; padding-left: 8px; padding-right: 8px;background-color: #5cb85c;border-color: #5cb85c;border-radius: 4px;border: 1px solid transparent; font-size: 14px;color: white;z-index: 999;width: 400px;height: 100px;'></div>");
    $('#loadPrompt').append("<i style='text-align: center; margin-bottom: 4px;display: block;width: 100%; margin-left: auto; margin-right: auto; font-size: 30px;'class='glyphicon glyphicon-upload'></i>");
    $('#loadPrompt').append("<h4 id='loadText' style='text-align: center;margin:auto;z-index: 999;color: white; display: block;'>Kép feltöltés és mentés folyamatban! Ne zárd be a lapot és ne kapcsold ki a gépet!</h4>");
}

function submitFinal() {
    $('#car_form').submit();
}

function uploadReady(uploadsFinished, numberOfUploads) {
    uploadsFinished += 1;
    if(uploadsFinished >= numberOfUploads) {
        submitFinal();
        return uploadsFinished;
    }
    return uploadsFinished;
}

function setInitialButtonListeners() {
    var initialButtonCells = $('.shuffle_cell');
    $(initialButtonCells).each(function() {
        setButtonClickListeners(this);
    });
}

function setButtonClickListeners(buttonCell) {
    setUpButtonListener($(buttonCell).find('.up_button'));
    setDownButtonListener($(buttonCell).find('.down_button'));
}

/*
upButton and downButton only modifies image_locations's content,
if it is a template-download row and
if the one that it is swapped with is also one.
the template-upload rows will get checked for their positions, once they were saved.
*/

function setUpButtonListener(button) {
    $(button).click(function() {
        var row = $(this).closest('tr');
        if ($(row).is(':first-child')) {
            return;
        }
        var rowAbove = $(row).prev('tr');

        //check if the row and the one above is a download
        changeDataPosition(row, rowAbove,'up');

        //swap the rows
        $(rowAbove).before(row);
    });
}

function setDownButtonListener(button) {
    $(button).click(function() {
        var row = $(this).closest('tr');
        if ($(row).is(':last-child')) {
            return;
        }
        var rowBelow = $(row).next('tr');

        //check if the row and the one below is a download
        changeDataPosition(row, rowBelow, 'down');

        //swap the rows
        $(rowBelow).after(row);
    });
}

function changeDataPosition(row, replacement, direction) {
    if(row.is('.template-download') && replacement.is('.template-download')){
        row.parent().children().each( function(index) {
            if (row.is(this)) {
                var data = JSON.parse($('#id_image_locations').val());
                var rowValue = data[String(index)];
                if (direction == 'up') {
                    data[String(index)] = data[String(index-1)];
                    data[String(index-1)] = rowValue;
                } else {
                    data[String(index)] = data[String(index+1)];
                    data[(index+1)] = rowValue;
                }
                $('#id_image_locations').val(JSON.stringify(data));
                return false;
            }
        });
    } else {
        return;
    }
}

//checks where the related row is, and returns the data of the new file and the old files in appropriate order
function savePosition(data) {
    olderData = $('#id_image_locations').val();
    jsonOlderData = JSON.parse(olderData);

    var updatedData;

    $('tbody').filter('.files').children().each( function(index){
        if ($(this).find('.name').children('a').text().trim() == data['0']['name']) {
            jsonOlderData.splice(index, 0, data['0']);
            updatedData = jsonOlderData;
            return false;
        }
    });
    return updatedData;
}

//ajax call to the server to request all the car ids and names
function getCarIdsAndNames() {
    $.ajax({
        url: "http://autohold.hu/getCars",
        data: {},
        dataType: 'json',
        success: function (data) {
            var selector = $('#template_selector');
            var jsonData = JSON.parse(data);
            var cars = jsonData['cars'];
            for (i = 0; i < cars.length; i++) {
                var id = cars[i]['id'];
                var name = cars[i]['name'];
                $(selector).append($("<option></option>")
                    .attr("value",id)
                    .text(name));
            }
        }
    });
}

function templateButtonClicked() {
    var id = $('#template_selector').find(":selected").attr("value");
    $.ajax({
        url: "http://autohold.hu/getCar/" + id,
        data: {},
        dataType: 'json',
        success: function (data) {
            var jsonData = JSON.parse(data);
            var fields = jsonData[0]['fields'];
            var fieldsToDelete = ['image_locations','futott','elsőforgalomba','ár', 'kiemeltajánlat', 'leírás', 'évjárat'];
            for (var i = 0; i < fieldsToDelete.length; i++) {
                delete fields[fieldsToDelete[i]];
            }
            var $form = $('#car_form');
            $.each( fields, function( key, value ) {
                var input = $form.find('#id_' + key);
                switch ($(input).prop('nodeName')){
                    case "INPUT":
                        if (input.attr("type") == "checkbox") {
                            if (value === true) {
                                input.prop("checked",true);
                            } else {
                                input.prop("checked",false);
                            }
                        } else {
                        input.val(value);
                        }
                        break;
                    case "SELECT":
                        input.val(value);
                        break;
                    default:
                        console.log("Assignment was unsuccessful: " + key + " : " + value);
                        break;
                }
            });
        }
    });
}

function checkAll() {
    var $form = $('#car_form');
    var $checkboxes = $( ":checkbox" ).not("#id_kiemeltajánlat");
    var allChecked = false;
    $.each($checkboxes, function() {
        if ($(this).prop("checked") === false) {
            $checkboxes.prop("checked", true);
            allChecked = true;
            return true;
        }
    });
    if (allChecked === false) {
        $checkboxes.prop("checked", false);
    }
}
