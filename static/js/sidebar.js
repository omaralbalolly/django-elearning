window.onresize = adjust_sidebar_height;
function adjust_sidebar_height(){
    // const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);
    var side_bar = document.querySelector('.side')
    // side_bar.style.height = `${vh}px`;
    var main_content = document.querySelector('.main_content');
    main_content.style.marginLeft = `${side_bar.offsetWidth}px`;
}
adjust_sidebar_height()