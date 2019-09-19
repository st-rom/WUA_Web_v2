import {Spinner} from './spin.js';


var width = 600;
var height = 380;
var a = [{level:1},{level:2},{level:3},{level:4}]

// a circle chart needs a radius
const koatuu = ['05', '07', '12', '14', '18', '21', '23', '26', '32', '35', '44', '46', '48', '51', '53', '56', '59', '61', '63', '65', '68', '71', '73', '74', '01']
const obls = ['Всі області', 'Вінницька область', 'Волинська область', 'Дніпропетровська область', 'Донецька область', 'Житомирська область', 'Закарпатська область', 'Запорізька область', 'Івано-Франківська область', 'Київська область', 'Кіровоградська область', 'Луганська область', 'Львівська область', 'Миколаївська область', 'Одеська область', 'Полтавська область', 'Рівненська область', 'Сумська область', 'Тернопільська область', 'Харківська область', 'Херсонська область', 'Хмельницька область', 'Черкаська область', 'Чернівецька область', 'Чернігівська область',  'АР Крим' ]
const years = ['2015', '2016', '2017', '2018', '2019']
const int_to_roman = {'1': 'І', '2': 'ІІ', '3': 'ІІІ', '4': 'ІV'}

let sel_city = document.getElementById('city-selector');
let sel_city_value = sel_city.value;
let sel_year_values = function (){
    const d = d3.selectAll('.ss-value-text')
    let vals = []
    d.each(function () {
        vals.push(this.innerText)
    })
    return vals
}();

var radius = Math.min(width, height) / 2;

var opts = {
    lines: 13, // The number of lines to draw
    length: 38, // The length of each line
    width: 17, // The line thickness
    radius: 45, // The radius of the inner circle
    scale: 1, // Scales overall size of the spinner
    corners: 1, // Corner roundness (0..1)
    color: 'black', // CSS color or array of colors
    fadeColor: 'transparent', // CSS color or array of colors
    speed: 1, // Rounds per second
    rotate: 0, // The rotation offset
    animation: 'spinner-line-fade-quick', // The CSS animation name for the lines
    direction: 1, // 1: clockwise, -1: counterclockwise
    zIndex: 2e9, // The z-index (defaults to 2000000000)
    className: 'spinner', // The CSS class to assign to the spinner
    top: '50%', // Top position relative to parent
    left: '50%', // Left position relative to parent
    shadow: '0 0 1px transparent', // Box-shadow for the lines
    position: 'fixed' // Element positioning
};

var target = document.getElementById('spinner');
var spinner = new Spinner(opts).spin(target);

// legend dimensions
var which_analytic = d3.select('.stat-selector__button:nth-child(3)')
which_analytic.attr('class', 'stat-selector__button stat-selector__button__selected')

var legendRectSize = 24; // defines the size of the colored squares in legend
var legendSpacing = 6; // defines spacing between squares

// define color scale
var colors = ['#69c242', '#64bbe3', '#ffcc00', '#ff7300'];
// var map = new Object({[1,2],[3,4]});


let dataset = new Object();

d3.select("#city-selector")
    .selectAll('option')
    .data(obls)
    .enter()
    .append('option')
    .text(d => d);


let main = function () {
    spinner.spin(target)
    if((sel_city_value !== sel_city.value) && (sel_city_value !== '')){
        // nx = 0;
        sel_city_value = sel_city.value;
        // sel_waste_value = sel_waste.value;
        // inp_num[0].value = 1;
        // inp_num[1].value = 10;
    }
    else if(sel_city_value !== sel_city.value){
        sel_city_value = sel_city.value;
        // sel_waste_value = sel_waste.value;
    }

    d3.select('#year-selector')
        .selectAll('option')
        .data(years)
        .enter()
        .append('option')
        .text(d => d)
        .attr('selected', '');


    new SlimSelect({
        select: '#year-selector',
        placeholder: 'Оберіть рік/роки',
        onChange: () => {
            sel_year_values = function (){
                const d = d3.selectAll('.ss-value-text')
                let vals = []
                d.each(function () {
                    vals.push(this.innerText)
                })
                return vals
            }();
            main();
        }
    })


    sel_year_values = function (){
        const d = d3.selectAll('.ss-value-text')
        let vals = []
        d.each(function () {
            vals.push(this.innerText)
        })
        return vals
    }();

    let data_filtered = data_all
    .filter(function(results){
        if (typeof koatuu[sel_city.selectedIndex] === 'object' && (results['fields']['koatuu'].startsWith(koatuu[sel_city.selectedIndex][0]) || results['fields']['koatuu'].startsWith(koatuu[sel_city.selectedIndex][1]))) {
            return true
        }
        return results['fields']['koatuu'].startsWith(koatuu[sel_city.selectedIndex]);
    })

    for (let i = 1; i < 5; i++) {
        let by_year_sum = 0
        for (let j = 0; j < sel_year_values.length; j++) {
            // console.log(typeof Math.round(results[sel_year_values[j] + '_' + sel_waste.options[sel_waste.selectedIndex].value] * 1000))
            by_year_sum += data_filtered.reduce( function(cnt,o){ return cnt + o['fields']['tonnes_' + i.toString() + '_' + sel_year_values[j]]; }, 0)
            // by_year_sum += results['fields']['tonnes_' + i.toString() + '_' + sel_year_values[j]]
        }
        dataset['Відходи ' + int_to_roman[i.toString()] + ' класу'] = by_year_sum
    }
    // console.log(dataset)


var color = d3.scaleOrdinal(colors);
// more color scales: https://bl.ocks.org/pstuffa/3393ff2711a53975040077b7453781a9
d3.select('#chart')
    .selectAll("*")
    .remove()


var svg = d3.select('#chart') // select element in the DOM with id 'chart'
    .append('svg') // append an svg element to the element we've selected
    .attr('width', width) // set the width of the svg element we just added
    .attr('height', height) // set the height of the svg element we just added
    .append('g') // append 'g' element to the svg element
    .attr('transform', 'translate(' + (width / 2 - 100)  + ',' + (height / 2) + ')'); // our reference is now to the 'g' element. centerting the 'g' element to the svg element


var arc = d3.arc()
  .innerRadius(0) // none for pie chart
  .outerRadius(radius); // size of overall chart

var pie = d3.pie() // start and end angles of the segments
  .value(function(d) { return d.count; }) // how to extract the numerical data from each entry in our dict
  .sort(null); // by default, data sorts in oescending value. this will mess with our animation so we set it to null

// define tooltip
var tooltip = d3.select('#chart') // select element in the DOM with id 'chart'
  .append('div') // append a div element to the element we've selected
  .attr('class', 'tooltip'); // add class 'tooltip' on the divs we just selected

tooltip.append('div') // add divs to the tooltip defined above
  .attr('class', 'label'); // add class 'label' on the selection

tooltip.append('div') // add divs to the tooltip defined above
  .attr('class', 'count'); // add class 'count' on the selection

tooltip.append('div') // add divs to the tooltip defined above
  .attr('class', 'percent'); // add class 'percent' on the selection

// Confused? see below:

// <div id="chart">
//   <div class="tooltip">
//     <div class="label">
//     </div>
//     <div class="count">
//     </div>
//     <div class="percent">
//     </div>
//   </div>
// </div>
var dict = []
for (var i = 0; i < 4; i++) {
    dict.push({
        label: Object.keys(dataset)[i],
        count: Object.values(dataset)[i]
    });
}

Object.values(dict).forEach(function(d) {
  d.count = +d.count; // calculate count as we iterate through the data
  d.enabled = true; // add enabled property to track which entries are checked
});
spinner.stop(target)

// creating the chart
var path = svg.selectAll('path') // select all path elements inside the svg. specifically the 'g' element. they don't exist yet but they will be created below
    .data(pie(dict)) //associate dict wit he path elements we're about to create. must pass through the pie function. it magically knows how to extract values and bakes it into the pie
    .enter() //creates placeholder nodes for each of the values
    .append('path') // replace placeholders with path elements
    .attr('d', arc) // define d attribute with arc function above
    .attr('fill', function(d) { return color(d.data.label); }) // use color scale to define fill of each label in dict
    .each(function(d) { this.current - d; }) // creates a smooth animation for each track
    // .append('title')
    // .attr('x', legendRectSize + legendSpacing)
    // .attr('y', legendRectSize - legendSpacing)
    // .text(function(d) { return d.droundata.label; });
                        // .style('max-width', 50)
    // .text(() =>  sel_waste.options[sel_waste.selectedIndex].value.endsWith('ПЗУВ') ? obls[i] + ': ' + (Math.round(obls_sum[i] ) / 1000).toString()     : obls[i] + ': ' + (Math.round(obls_sum[i] ) / 1000).toString() + ' kтонн (* 10^3)');


// mouse event handlers are attached to path so they need to come after its definition
path.on('mouseover', function(d) {  // when mouse enters div
 var total = d3.sum(dict.map(function(d) { // calculate the total number of tickets in the dict
  return (d.enabled) ? d.count : 0; // checking to see if the entry is enabled. if it isn't, we return 0 and cause other percentages to increase
  }));
 var percent = Math.round(1000 * d.data.count / total) / 10; // calculate percent
 tooltip.select('.label').html(d.data.label); // set current label
 tooltip.select('.count').html((Math.round(parseFloat(d.data.count) * 1000) / 1000).toString() + ' тонн'); // set current count
 // tooltip.select('.percent').html(percent + '%'); // set percent calculated above
 tooltip.style('display', 'block'); // set display
});

path.on('mouseout', function() { // when mouse leaves div
  tooltip.style('display', 'none'); // hide tooltip for that element
 });

path.on('mousemove', function(d) { // when mouse moves
  tooltip.style('top', (d3.event.layerY + 10) + 'px') // always 10px below the cursor
    .style('left', (d3.event.layerX + 10) + 'px'); // always 10px to the right of the mouse
  });

// define legend
var legend = svg.selectAll('.legend') // selecting elements with class 'legend'
  .data(color.domain()) // refers to an array of labels from our dict
  .enter() // creates placeholder
  .append('g') // replace placeholders with g elements
  .attr('class', 'legend') // each g is given a legend class
  .attr('transform', function(d, i) {
    var height = legendRectSize + legendSpacing; // height of element is the height of the colored square plus the spacing
    var offset =  height * color.domain().length / 2; // vertical offset of the entire legend = height of a single element & half the total number of elements
    var horz = 10 * legendRectSize; // the legend is shifted to the left to make room for the text
    var vert = i * height - offset; // the top of the element is hifted up or down from the center using the offset defiend earlier and the index of the current element 'i'
      return 'translate(' + horz + ',' + vert + ')'; //return translation
   });

// adding colored squares to legend
legend.append('rect') // append rectangle squares to legend
  .attr('width', legendRectSize) // width of rect size is defined above
  .attr('height', legendRectSize) // height of rect size is defined above
  .style('fill', color) // each fill is passed a color
  .style('stroke', color) // each stroke is passed a color
  .on('click', function(label) {
    var rect = d3.select(this); // this refers to the colored squared just clicked
    var enabled = true; // set enabled true to default
    var totalEnabled = d3.sum(dict.map(function(d) { // can't disable all options
      return (d.enabled) ? 1 : 0; // return 1 for each enabled entry. and summing it up
    }));

    if (rect.attr('class') === 'disabled') { // if class is disabled
      rect.attr('class', ''); // remove class disabled
    } else { // else
      if (totalEnabled < 2) return;// if less than two labels are flagged, exit
      rect.attr('class', 'disabled'); // otherwise flag the square disabled
      enabled = false; // set enabled to false
    }

    pie.value(function(d) {
      if (d.label === label) d.enabled = enabled; // if entry label matches legend label
        return (d.enabled) ? d.count : 0; // update enabled property and return count or 0 based on the entry's status
    });

    path = path.data(pie(dict)); // update pie with new data

    path.transition() // transition of redrawn pie
      .duration(750) //
      .attrTween('d', function(d) { // 'd' specifies the d attribute that we'll be animating
        var interpolate = d3.interpolate(this._current, d); // this = current path element
        this._current = interpolate(0); // interpolate between current value and the new value of 'd'
        return function(t) {
          return arc(interpolate(t));
        };
      });
  });

// adding text to legend
legend.append('text')
  .attr('x', legendRectSize + legendSpacing)
  .attr('y', legendRectSize - legendSpacing)
  .text(function(d) { return d; }); // return label


};

sel_city.addEventListener("click", main);
sel_city.click()

// console.log(data_all[0]['fields'])

// .filter(function (results) {
//     if
// })
//     .map(function (results) {
//         let dataset = {}
//         for (let i = 0; i < 4; i++) {
//             let by_year_sum = 0
//             for (let j = 0; j < sel_year_values.length; j++) {
//                 // console.log(typeof Math.round(results[sel_year_values[j] + '_' + sel_waste.options[sel_waste.selectedIndex].value] * 1000))
//                 by_year_sum += results['fields']['tonnes_' + i.toString() + sel_year_values[j]]
//             }
//             dataset['class ' + i.toString()] = by_year_sum
//         }
//         return dataset
//         // return [results.Name, Math.round(by_year_sum * 1000) / 1000, results.EDRPOU, results.KOATUU];
//
//     })
    // .sort(function(a, b){
    //     return b[1]-a[1]
    // })
// function (results) {

// console.log(dataset)

// dataset = data_all
