function addDetailstotask(){
    document.getElementById('add_details_task').style.display = 'block';
    document.getElementById('btn_add_details_task').style.display = 'none';
    document.getElementById('add_new_category').style.display = 'none';
}
function closeAddDetailsTask() {
    document.getElementById('add_details_task').style.display = 'none';
    document.getElementById('btn_add_details_task').style.display = 'inline-block';
}
function addNewCategory(){
    document.getElementById('add_new_category').style.display = 'block';
    document.getElementById('btn_add_new_category').style.display = 'none';
    document.getElementById('add_new_task').style.display = 'none';
}
function closeAddNewCategory(){
    document.getElementById('add_new_category').style.display = 'none';
    document.getElementById('btn_add_new_category').style.display = 'inline-block';
    document.getElementById('add_new_task').style.display = 'block';
}
function addDateTime(){
    document.getElementById('add_date_time').style.display = 'block';
    document.getElementById('btn_add_date_time').style.display = 'none';
    document.getElementById('add_new_category').style.display = 'none';
}
function closeAddDateTime() {
    document.getElementById('add_date_time').style.display = 'none';
    document.getElementById('btn_add_date_time').style.display = 'inline-block';

}
function show_tasks() {
    if (getComputedStyle(document.getElementById('tasks')).display == 'inline-block') {    //if tasks in page, hide tasks
        document.getElementById('tasks').style.display = 'none';                    //and show notes in all page
        document.getElementById('btn_tasks').style.width = '15%';
        document.getElementById('btn_tasks_h').style.opacity = '70%';
        document.getElementById('notes').style.width = '100%';
        document.getElementById('notes').style.display = 'flex';
        document.getElementById('btn_notes').style.width = '70%';
        document.getElementById('div_near_btn_notes').style.display = 'inline-block';
        document.getElementById('div_near_btn_tasks').style.display = 'none';
        document.getElementById('btn_notes_h').style.opacity = '100%';
    } else {
        document.getElementById('tasks').style.display = 'inline-block';
        document.getElementById('notes').style.width = '50%';                       //if tasks hided, show tasks in 1/2 page.
        document.getElementById('tasks').style.width = '50%';
        document.getElementById('div_near_btn_notes').style.display = 'none';
        document.getElementById('btn_tasks').style.width = '50%';
        document.getElementById('btn_notes').style.width = '50%';
        
    }
}
function show_notes() {
    if (getComputedStyle(document.getElementById('notes')).display == 'flex') {    //if notes in page, hide notes
        document.getElementById('notes').style.display = 'none';                    //and show tasks in all page
        document.getElementById('btn_notes').style.width = '15%';
        document.getElementById('btn_notes_h').style.opacity = '70%';
        document.getElementById('tasks').style.display = 'inline-block';
        document.getElementById('tasks').style.width = '100%';
        document.getElementById('btn_tasks').style.width = '70%';
        document.getElementById('div_near_btn_tasks').style.display = 'inline-block';
        document.getElementById('div_near_btn_notes').style.display = 'none';
        document.getElementById('btn_notes').style.width = '15%';
        document.getElementById('btn_tasks_h').style.opacity = '100%';
    } else {
        document.getElementById('notes').style.display = 'flex';
        document.getElementById('tasks').style.width = '50%';   //if tasks hided, show tasks in 1/2 page.
        document.getElementById('notes').style.width = '50%';
        document.getElementById('div_near_btn_tasks').style.display = 'none';
        document.getElementById('btn_notes').style.width = '50%';
        document.getElementById('btn_tasks').style.width = '50%';
        document.getElementById('btn_tasks_h').style.opacity = '100%';
        document.getElementById('btn_notes_h').style.opacity = '100%';
        
    }
}

function accountMenu() {
    if (getComputedStyle(document.getElementById('account_menu')).display == 'none') {
        document.getElementById('account_menu').style.display = 'block';
    }
    else {
        document.getElementById('account_menu').style.display = 'none';
    }
}