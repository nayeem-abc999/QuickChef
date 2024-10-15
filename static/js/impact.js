var yourGoal = "";



document.getElementById("set-your-goal").addEventListener("click", ()=>{
    document.getElementById("set-field").style.display = "block"
  document.getElementById("set-your-goal").style.display = "none"
})

document.getElementById("cancel-btn").addEventListener("click",()=>{
    document.getElementById("set-field").style.display = "none"
  document.getElementById("set-your-goal").style.display = "block";
})
document.getElementById("cancel-btn").addEventListener("click",()=>{
    document.getElementById("set-field").style.display = "none"
  document.getElementById("set-your-goal").style.display = "block";
})

document.getElementById("save-btn").addEventListener("click",()=>{
    const goal = document.getElementById("inputText").value;
    yourGoal = goal;
    if(goal != ""){    
        document.getElementById("add-goal-title").innerHTML  = "My goal is to..."
        document.getElementById("set-your-goal").innerHTML = yourGoal
    }
    else{
        document.getElementById("add-goal-title").innerHTML  = "Add your motivation for using Kitche"
        document.getElementById("set-your-goal").innerHTML = "Set your goal" 
    }
    document.getElementById("set-field").style.display = "none"
    document.getElementById("set-your-goal").style.display = "block"
})
//chart
var ctx = document.getElementById('line-chart').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [{
      label: 'Weekly waste cost',
      data: [10, 5, 4, 0, 9, 6, 6],
      borderColor: "#c2cfd5",
      borderWidth: 2,
      pointBackgroundColor: 'white',
      fill: false
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});
// Active function to switch between pages
function activate1() {
    document.getElementById("sum-text").style.color  = "white";
    document.getElementById("awards-text").style.color  = "black";
    document.getElementById("summary-btn").style.backgroundColor = "#02a284";
    document.getElementById("awards-btn").style.backgroundColor  = "#eaeef0";
    document.getElementById("summary-field").classList.add("active1");
    document.getElementById("awards-field").classList.remove("active2");
}

function activate2() {
    document.getElementById("awards-text").style.color  = "white";
    document.getElementById("sum-text").style.color  = "black";
    document.getElementById("summary-btn").style.backgroundColor  = "#eaeef0"
    document.getElementById("awards-btn").style.backgroundColor = "#02a284"
    document.getElementById("awards-field").classList.add("active2");
    document.getElementById("summary-field").classList.remove("active1");
}   

function activate3() {
    document.getElementById("thisweek-child-text").style.color  = "white";
    document.getElementById("lastweek-child-text").style.color  = "black";
    document.getElementById("thisweek-btn").style.backgroundColor = "#02a284";
    document.getElementById("lastweek-btn").style.backgroundColor  = "#eaeef0";
    document.getElementById("thisweek-text").classList.add("active3");
    document.getElementById("lastweek-text").classList.remove("active4");
}

function activate4() {
    document.getElementById("lastweek-child-text").style.color  = "white";
    document.getElementById("thisweek-child-text").style.color  = "black";
    document.getElementById("thisweek-btn").style.backgroundColor  = "#eaeef0"
    document.getElementById("lastweek-btn").style.backgroundColor = "#02a284"
    document.getElementById("lastweek-text").classList.add("active4");
    document.getElementById("thisweek-text").classList.remove("active3");
}   

function activate5() {
    document.getElementById("achieve-child-text").style.color  = "white";
    document.getElementById("goal-child-text").style.color  = "black";
    document.getElementById("achieve-btn").style.backgroundColor = "#02a284";
    document.getElementById("goal-btn").style.backgroundColor  = "#eaeef0";
    document.getElementById("achievement").style.display = "block";
    document.getElementById("goal").style.display = "none";
}

function activate6() {
    document.getElementById("goal-child-text").style.color  = "white";
    document.getElementById("achieve-child-text").style.color  = "black";
    document.getElementById("achieve-btn").style.backgroundColor  = "#eaeef0"
    document.getElementById("goal-btn").style.backgroundColor = "#02a284"
    document.getElementById("achievement").style.display = "none";
    document.getElementById("goal").style.display = "block";
}   

