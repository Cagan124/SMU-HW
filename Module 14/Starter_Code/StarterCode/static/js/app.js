// add url
let url = "https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json"
// get data from json
let global_data
d3.json(url).then(function(data) {
    console.log(data);
    global_data = data;
  // add dropdown using d3
  let dropdownmenu = d3.select("#selDataset");
  // use for loop for dropdown
    for (let i = 0; i < data.names.length; i++){
    let name = data.names[i];
    dropdownmenu.append("option").text(name);
}
// assign the data to the names
    let human = data.names[0];
    let human_data = data.samples.filter(row => row.id === human)[0];
    console.log(human_data);

    makeBar(human_data);
    makeBubble(human_data);
});
// create bar chart
function makeBar(human_data) {
    let sampleValues = human_data.sample_values.slice(0,10).reverse();
    let otuIDs = human_data.otu_ids.slice(0,10).reverse();
    let otuLabels = human_data.otu_labels.slice(0,10).reverse();

    let trace = {
        x: sampleValues,
        y: otuIDs.map(id => `OTU ${id}`),
        text: otuLabels,
        type: "bar",
        orientation: "h"
    };

    let traces = [trace]

    let layout = {
        title: "Top 10 OTUs",
        xaxis: {title: "Sample Values"},
        yaxis: {title: "OTU IDs"}
    };

    Plotly.newPlot("bar", traces, layout);
}

function optionChanged(human) {
    let human_data = global_data.samples.filter(row => row.id === human)[0];
    console.log(human_data)
}

// create bubble chart

function makeBubble(human_data) {

    let sampleValues = human_data.sample_values;
    let otuIDs = human_data.otu_ids;
    let otuLabels = human_data.otu_labels;


    let trace1= {
        x: [otuIDs],
        y: [sampleValues],
        mode: 'markers',
        marker: {
            size: [sampleValues],
            color: ['rgb(255, 65, 54)'],
            opacity: [1]
        },
        text: otuLabels
    }

    let traces2 = [trace1];

    let layout = {
        title: "Belly Button Data",
        showlegend: false,
        height: 600,
        width: 600
    };
    Plotly.newPlot('bubble', traces2, layout)
};

