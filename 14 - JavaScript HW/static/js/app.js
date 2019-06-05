// from data.js
var tableData = data;

// Get a reference to the table body
var tbody = d3.select("tbody");

//Approach 2 - Looping Through Keys in Object

function DisplayTableRowsLooped(someData){
    var row = tbody.append("tr");
    var theKeys = Object.keys(someData);
    for (var i = 0; i <theKeys.length; i = i + 1){
        row.append("td").text(someData[theKeys[i]]);
    }
}


//Empty the Table
//tbody.text("");
//Write data to table using Approach 2
tableData.forEach(DisplayTableRowsLooped);


// Select the filter button
var submit = d3.select("#filter-btn");

// initialize form input global variable
// var forminput = "";

//filter function for datetime according to forminput
function filterdateTime(ldata) {
  return ldata.datetime === forminput;
}

submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  //set equal to global variable form input
  forminput = inputValue;

  //filter according to datetime - used filter datetime function
  tableData.filter(filterdateTime);

  var filteredData = tableData.filter(dt => dt.datetime === inputValue);

  tbody.text("");
  filteredData.forEach(DisplayTableRowsLooped);

});


