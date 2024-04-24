$(function () {

  function Last_Week_Data() {

    return {
      labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"],
      datasets: [{
        label: '# of Sales',
        data: [10, 19, 3, 5, 2, 3, 8],
        backgroundColor: ['rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(255, 159, 64, 0.2)'],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1,
        fill: false
      }]
    };
  }
  function Last_Month_Data() {
    return {
      labels: ["1st Week", "2nd Week", "3rd Week", "4th Week"],
      datasets: [{
        label: '# of Sales',
        data: [7, 3, 9, 2],
        backgroundColor: ['rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)'],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)'],
        borderWidth: 1,
        fill: false
      }]
    };
  }
  function Last_Two_Month_Data() {

    return {
      labels: ["1st Week", "2nd Week", "3rd Week", "4th Week", "5th Week", "6th Week", "7th Week", "8th Week"],
      datasets: [{
        label: '# of Sales',
        data: [7, 3, 9, 2, 6, 8, 5, 4], // Sample data for the last 8 weeks
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(128, 0, 128, 0.2)', // Purple
          'rgba(0, 128, 128, 0.2)', // Teal
        ],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(128, 0, 128, 1)', // Purple
          'rgba(0, 128, 128, 1)', // Teal
        ],
        borderWidth: 1,
        fill: false
      }]
    };
  }
  function Last_Year_Data() {
    return {
        labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        datasets: [{
            label: '# of Sales',
            data: [100, 120, 90, 80, 110, 130, 140, 150, 120, 110, 100, 130], // Sample data for each month of the year
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',    // Red
                'rgba(54, 162, 235, 0.2)',    // Blue
                'rgba(255, 206, 86, 0.2)',    // Yellow
                'rgba(75, 192, 192, 0.2)',    // Aqua
                'rgba(153, 102, 255, 0.2)',   // Purple
                'rgba(255, 159, 64, 0.2)',    // Orange
                'rgba(255, 205, 86, 0.2)',    // Gold
                'rgba(54, 162, 235, 0.2)',    // Blue
                'rgba(255, 99, 132, 0.2)',    // Red
                'rgba(75, 192, 192, 0.2)',    // Aqua
                'rgba(153, 102, 255, 0.2)',   // Purple
                'rgba(255, 159, 64, 0.2)'     // Orange
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 205, 86, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,
            fill: false
        }]
    };
}

  function Last_Week_Data_Area() {

    return {
      labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"],
      datasets: [{
        label: '# of Sales',
        data: [10, 19, 3, 5, 2, 3, 8],
        backgroundColor: ['rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(255, 159, 64, 0.2)'],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1,
        fill: true
      }]
    };
  }
  function Last_Month_Data_Area() {

    return {
      labels: ["1st Week", "2nd Week", "3rd Week", "4th Week"],
      datasets: [{
        label: '# of Sales',
        data: [7, 3, 9, 2],
        backgroundColor: ['rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)'],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)'],
        borderWidth: 1,
        fill: true
      }]
    };
  }

  function Last_Two_Month_Data_Area() {
    return {
      labels: ["1st Week", "2nd Week", "3rd Week", "4th Week", "5th Week", "6th Week", "7th Week", "8th Week"],
      datasets: [{
        label: '# of Sales',
        data: [7, 3, 9, 2, 6, 8, 5, 4], // Sample data for the last 8 weeks
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(128, 0, 128, 0.2)', // Purple
          'rgba(0, 128, 128, 0.2)', // Teal
        ],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(128, 0, 128, 1)', // Purple
          'rgba(0, 128, 128, 1)', // Teal
        ],
        borderWidth: 1,
        fill: true
      }]
    };
  }
  function Last_Year_Data_Area() {
    return {
        labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        datasets: [{
            label: '# of Sales',
            data: [100, 120, 90, 80, 110, 130, 140, 150, 120, 110, 100, 130], // Sample data for each month of the year
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',    // Red
                'rgba(54, 162, 235, 0.2)',    // Blue
                'rgba(255, 206, 86, 0.2)',    // Yellow
                'rgba(75, 192, 192, 0.2)',    // Aqua
                'rgba(153, 102, 255, 0.2)',   // Purple
                'rgba(255, 159, 64, 0.2)',    // Orange
                'rgba(255, 205, 86, 0.2)',    // Gold
                'rgba(54, 162, 235, 0.2)',    // Blue
                'rgba(255, 99, 132, 0.2)',    // Red
                'rgba(75, 192, 192, 0.2)',    // Aqua
                'rgba(153, 102, 255, 0.2)',   // Purple
                'rgba(255, 159, 64, 0.2)'     // Orange
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 205, 86, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,
            fill: true
        }]
    };
}

  function Doughnut_Data() {
    return {
      datasets: [{
        data: [30, 40, 30],
        backgroundColor: [
          'rgba(255, 99, 132, 0.5)',
          'rgba(54, 162, 235, 0.5)',
          'rgba(255, 206, 86, 0.5)',
          'rgba(75, 192, 192, 0.5)',
          'rgba(153, 102, 255, 0.5)',
          'rgba(255, 159, 64, 0.5)'
        ],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
      }],
      labels: [
        'Pink',
        'Blue',
        'Yellow',
      ]
    };
  }


  function updateChartData(interval) {
    var newData;
    var areaData;
    var doughnutData;
    if (interval === '1 Week') {
      newData = Last_Week_Data();
      areaData = Last_Week_Data_Area();
      doughnutData = Doughnut_Data();
    } else if (interval === '4 Week') {
      newData = Last_Month_Data();
      areaData = Last_Month_Data_Area();
      doughnutData = Doughnut_Data();
    } else if (interval === '8 Week') {
      newData = Last_Two_Month_Data();
      areaData = Last_Two_Month_Data_Area();
      doughnutData = Doughnut_Data();
    } else if (interval === '1 Year') {
      newData = Last_Year_Data();
      areaData = Last_Year_Data_Area();
      doughnutData = Doughnut_Data();
    }

    if (newData) {
      barChart.data = newData;
      barChart.update();

      areaChart.data = areaData;
      areaChart.update();

      lineChart.data = newData;
      lineChart.update();

      doughnutChart.data = doughnutData;
      doughnutChart.update();

      pieChart.data = doughnutData;
      pieChart.update();
    }
  }
  $('.dropdown-item').on('click', function () {
    var interval = $(this).text();
    updateChartData(interval);
  });


  var initialData = {
    labels: ["Initial Label"],
    datasets: [{
      label: 'Initial Dataset',
      data: [0],
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1
    }]
  };

  var options = {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    },
    legend: {
      display: false
    },
    elements: {
      point: {
        radius: 0
      }
    }
  };

  var areaOptions = {
    plugins: {
      filler: {
        propagate: true
      }
    }
  }

  var doughnutPieOptions = {
    responsive: true,
    animation: {
      animateScale: true,
      animateRotate: true
    }
  };

  var barChartCanvas = $("#barChart").get(0).getContext("2d");
  var barChart = new Chart(barChartCanvas, {
    type: 'bar',
    data: initialData,
    options: options
  });
  var areaChartCanvas = $("#areaChart").get(0).getContext("2d");
  var areaChart = new Chart(areaChartCanvas, {
    type: 'line',
    data: initialData,
    options: areaOptions
  });
  var lineChartCanvas = $("#lineChart").get(0).getContext("2d");
  var lineChart = new Chart(lineChartCanvas, {
    type: 'line',
    data: initialData,
    options: options
  });
  var doughnutChartCanvas = $("#doughnutChart").get(0).getContext("2d");
  var doughnutChart = new Chart(doughnutChartCanvas, {
    type: 'doughnut',
    data: initialData,
    options: doughnutPieOptions
  });
  var pieChartCanvas = $("#pieChart").get(0).getContext("2d");
  var pieChart = new Chart(pieChartCanvas, {
    type: 'pie',
    data: initialData,
    options: doughnutPieOptions
  });

});
