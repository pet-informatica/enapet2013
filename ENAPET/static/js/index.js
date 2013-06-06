$(document).ready(function(){
  JBCountDown({
    secondsColor : "#ffdc50",
    secondsGlow  : "none",

    minutesColor : "#9cdb7d",
    minutesGlow  : "none",

    hoursColor   : "#378cff",
    hoursGlow    : "none",

    daysColor    : "#ff6565",
    daysGlow     : "none",

    startDate   : "1380614400",
    endDate     : "1380996000",
    now         : Math.floor((new Date).getTime()/1000),
  });
});
