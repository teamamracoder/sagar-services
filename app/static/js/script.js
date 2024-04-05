"use strict";

console.log("welcome to sagar services");

const getFormattedDateTime = (datetime)=>{
    let date = new Date(datetime);
    let options = {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        hour12: true
    };
    let formattedDate = date.toLocaleString('en-GB', options);
    return(formattedDate);
}