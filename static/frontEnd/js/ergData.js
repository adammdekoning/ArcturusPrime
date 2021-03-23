console.log('ergdata.js is connected')

const columnDefs = [
  { field: "date", sortable: true, filter: true },
  { field: "crew", sortable: true, filter: true },
  { field: "distance", sortable: true, filter: true },
  { field: "time", sortable: true, filter: true},
  { field: "rate", sortable: true, filter: true},
  { field: "notes", sortable: true, filter: true}
];

// const rowData = [
//   { date: "2021-03-10", name: "Alex Nell", distance: 2000, time: "00:07:20.1"}
// ]

const gridOptions = {
  columnDefs: columnDefs,
  // rowData: rowData
};

document.addEventListener('DOMContentLoaded', () => {
  const egridDiv = document.querySelector('#ergGrid');
  new agGrid.Grid(egridDiv, gridOptions);
})

agGrid.simpleHttpRequest({url: 'http://127.0.0.1:8000/backend/ergResultsList/'}).then(data => {
    gridOptions.api.setRowData(data);
});
