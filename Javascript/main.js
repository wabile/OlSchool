let educationCount = 1;

function addEducation() {
    educationCount++;
    const container = $("#educations-container");

    const div = $("<div>").addClass("form-row education-row");

    const educationCol = $("<div>").addClass("col-6");
    const educationLabel = $("<label>").addClass("form-label mt-3 mb-2").text(`Education ${educationCount}:`);
    const educationInput = $("<input>").addClass("form-control education-input").attr("id", `education${educationCount}`).attr("name", `education${educationCount}`).attr("required", "required");

    const institutionCol = $("<div>").addClass("col-5 mt-3 mb-2");
    const institutionLabel = $("<label>").addClass("form-label").text("Institution:");
    const institutionInput = $("<input>").addClass("form-control institution-input").attr("id", `institution${educationCount}`).attr("name", `institution${educationCount}`).attr("required", "required");

    const removeButtonCol = $("<div>").addClass("col-1 align-self-center").css({position: 'relative'});
    const removeButton = $("<button>").addClass("btn btn-outline-danger remove-education").attr("type", "button").html('<i class="fas fa-trash"></i>').css({position: 'absolute', top: "1px", right: "1px"});

    container.append(div);
    div.append(educationCol);
    educationCol.append(educationLabel);
    educationCol.append(educationInput);
    div.append(institutionCol);
    institutionCol.append(institutionLabel);
    institutionCol.append(institutionInput);
    div.append(removeButtonCol);
    removeButtonCol.append(removeButton);
}

function removeEducation() {
    $(this).closest(".education-row").remove();
    educationCount--;
}

$("#add-education-button").on("click", addEducation);
$("#educations-container").on("click", ".remove-education", removeEducation);



let scheduleCount = 1;

function addScheduleField() {
    scheduleCount++;

    let newField = `
        <div class="form-group schedule-field">
            <div class="form-row align-items-center">
                <div class="col-md-4 mb-3">
                    <label for="class-date-${scheduleCount}">Class Date:</label>
                    <div class="input-group">
                        <input type="date" class="form-control" id="class-date-${scheduleCount}" name="class_date[]" required>
                    </div>
                </div>
                <div class="col-md-4 mb-3">
                    <label for="class-time-${scheduleCount}">Class Time:</label>
                    <div class="input-group">
                        <input type="time" class="form-control" id="class-time-${scheduleCount}" name="class_time[]" required>
                    </div>
                </div>
                <div class="col-md-4 mb-3">
                    <label for="class-duration-${scheduleCount}">Class Duration:</label>
                    <div class="input-group">
                        <input type="number" class="form-control" id="class-duration-${scheduleCount}" name="class_duration[]" placeholder="in minutes" required>
                        <div class="input-group-append">
                            <button class="btn btn-outline-danger remove-schedule-field" type="button">
                                <i class="fas fa-trash"></i>
                            </button>
                        </div>
                        <div class="input-group-append">
                        <button class="btn btn-outline-secondary add-schedule-field" type="button">
                            <i class="fas fa-plus"></i>
                        </button>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    `;

    $(".schedule-fields").append(newField);
}

function removeScheduleField() {
    $(this).closest(".schedule-field").remove();
}

$(document).on("click", ".add-schedule-field", addScheduleField);
$(document).on("click", ".remove-schedule-field", removeScheduleField);