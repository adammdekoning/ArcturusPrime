console.log('master.js file connected')





function goBack() {
  window.history.back();
}





resultsList()

function resultsList(){

  var session_dates = document.getElementsByClassName("session_date");
  var n

  for (n=0; n < session_dates.length; n++) {
    session_dates[n].addEventListener("click", function(){

      var session_id = this.id
      var session_info = this.innerHTML
      console.log(session_id)


      results_window = document.getElementById("results_window")
      results_window.innerHTML = `
      <div class="card card-body" >
      <h3>${session_info}</h3>
      <table id="sortable_results_table" class="table table-striped">
        <thead>
          <tr id = "results_header">
            <th>Crew</th>
            <th>Distance</th>
            <th>Avg Time</th>
            <th>Avg Split</th>
          </tr>
        </thead>

        <tbody id=results_table>
        </tbody>
      </table>
      </div>
        `
      results_table = document.getElementById("results_table")
      results_header = document.getElementById("results_header")

      var url = `http://127.0.0.1:8000/backend/session_results_json/${session_id}/`

      fetch(url)
      .then((resp) => resp.json())
      .then(function(data){
        console.log('Data:', data)

        var list = data

        var p = 1
        for (var i in list){
          if (list[i].pieces > p){
            p = list[i].pieces
          }
        }
        for (n=1; n < (p + 1); n++) {
          results_header.innerHTML += `<th>Piece ${n}</th>`
        }
        for (var i in list){

          var crew = list[i].crew
          var distance = list[i].distance
          var average_time = list[i].average_time
          var average_split = list[i].average_split
          for (n=1; n < (list[i].pieces + 1); n++) {
            eval('var piece_' + n + '= list[i].piece_' + n + ';')
          }

          line = `
          <tr id="result_row${i}">
            <td>${crew}</td>
            <td>${distance}</td>
            <td>${average_time}</td>
            <td>${average_split}</td>
          </tr>
          `

          results_table.innerHTML += line

          result_row = document.getElementById(`result_row${i}`)

          for (n=1; n < (p+1); n++){
            var a = eval('piece_' + n +';');
            result_row.innerHTML += `  <td>${a}</td>`
            console.log(a)
          }


        }
        // for (n=1; n < (p + 1); n++) {
        //   results_header.innerHTML += `<th>Piece ${n}</th>`
        // }
      }
    )
    })
  }

}
