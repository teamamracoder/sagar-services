"use strict";

console.log("welcome to sagar services");

const getFormattedDateTime = (datetime)=>{
    let date = new Date(datetime);
    let options = {
        timeZone: 'UTC',
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        hour12: true
    };
    let formattedDate = date.toLocaleString('en-GB', options);
    return(formattedDate);
};

const getFormattedTime = (datetime)=>{
    let date = new Date(datetime);
    let options = {
        hour: 'numeric',
        minute: 'numeric',
        hour12: true
    };
    let formattedTime = date.toLocaleString('en-GB', options);
    return(formattedTime);
};


// nav transparent
// $(document).ready(function(){
//     $(window).scroll(function(){
//       if($(this).scrollTop() > 50){
//         $('#nav').css('background', 'linear-gradient(to top left, #8fbfef, #2178cf)');
//         $('.nav-link').css('color', '#fff');
//       } else {
//         $('.nav-link').css('color', '#000');
//         $('#nav').css('background', 'transparent');
//       }
//     });
//   });
