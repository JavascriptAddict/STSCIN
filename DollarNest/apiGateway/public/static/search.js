
async function fetchJsonData(url) {
    try {
        const response = await fetch(url);
        
        // Check if the response is ok (status code 200–299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        // Parse JSON data
        const data = await response.json();
        return data;
        
    } catch (error) {
        console.error("Error fetching JSON data:", error);
        return null; // Return null or handle error as needed
    }
  }
  
  window.addEventListener("load", (event) => {
    var recentTransactionsTable = document.getElementById("transactionDiv");
    fetchJsonData('http://localhost/estate')
    .then(data => {
        if (data) {
            var html = "";
            data = data.data.estates;
            for(var count=0; count < data.length; count++){
              html += `<tr>
                        <td>${data[count].residenceName}</td>
                        <td>${data[count].area}</td>
                        <td>${data[count].state}</td>
                        <td>${data[count].type}</td>
                        <td>${data[count].transactionDate}</td>
                        <td>${data[count].price}</td>
                      </tr>`
            }
            recentTransactionsTable.innerHTML = html;
            updateInsights();
            // Handle data here
        } else {
            console.log("No data found.");
        }
    });
  });

  function applyFilter(){
    var state = document.getElementById("state").value;
    var type = document.getElementById("type").value;
    var residence = document.getElementById("residence").value;
    var startTransaction = document.getElementById("start-transaction-date").value;
    var endTransaction = document.getElementById("end-transaction-date").value;
    var transactionsDiv = document.getElementById("transactionDiv");

    query = ""

    if(state != "Choose..." && state != null){
        query += `state=${state}&`;
    }
    if(type != "Choose..." &&  type != null){
        query += `type=${type}&`;
    }
    if(residence != "" &&  residence != null){
        query += `residenceName=${residence}&`;
    }
    if(startTransaction != "" &&  startTransaction != null){
        query += `startTransactionDate=${startTransaction}&`;
    }
    if(endTransaction != "" && endTransaction != null){
        query += `endTransactionDate=${endTransaction}&`;
    }

    fetchJsonData(`http://localhost/estate/filtered?${query}`)
    .then(data => {
        try{
            if (data.data.estates) {
                var html = "";
                data = data.data.estates;
                for(var count=0; count < data.length; count++){
                 html += `<tr>
                            <td>${data[count].residenceName}</td>
                            <td>${data[count].area}</td>
                            <td>${data[count].state}</td>
                            <td>${data[count].type}</td>
                            <td>${data[count].transactionDate}</td>
                            <td>${data[count].price}</td>
                          </tr>`
                }
                transactionsDiv.innerHTML = html;
                // Handle data here
                updateInsights();
            }
        }catch{
            updateInsights(1);
            console.log("No data found.");
            transactionsDiv.innerHTML = "<div class='text-center'>No records found.</div>";
        }
        
    });

  }

  async function downloadPDF() {
    const { jsPDF } = window.jspdf;
  
    const canvas = await html2canvas(document.body, {
      scale: 2,
      useCORS: true  // Enable cross-origin requests for images
    });
    const imgData = canvas.toDataURL("image/png");
  
    const pdf = new jsPDF("p", "mm", "a4");
    const pdfWidth = pdf.internal.pageSize.getWidth();
    const pdfHeight = (canvas.height * pdfWidth) / canvas.width;
  
    pdf.addImage(imgData, "PNG", 0, 0, pdfWidth, pdfHeight);
    pdf.save("full-page.pdf");
  }
  
  //funtion to update insights card
  function updateInsights(error=null) {
    const rows = document.querySelectorAll("#transactionDiv tr");
    if (error != null) {
      document.getElementById("highest-price").querySelector("b").textContent = "$0";
      document.getElementById("total-sales").querySelector("b").textContent = "0 Units";
      document.getElementById("average-price").querySelector("b").textContent = "$0";
      return;
    }

    const prices = [];
    
    // Loop through each row to get prices
    rows.forEach((row) => {
      const cells = row.querySelectorAll("td");
      const priceStr = cells[5]?.textContent.trim().replace(/[$,]/g, ""); // Price (remove $ and commas)
      const price = parseFloat(priceStr);
  
      if (!isNaN(price)) {
        prices.push(price);
      }
    });
  
    // Calculate insights
    const highestSoldPrice = prices.length ? Math.max(...prices).toLocaleString("en-US", { style: "currency", currency: "USD" }) : "$0";
    const totalSales = rows.length; // Total number of rows
    const averagePrice = prices.length ? (prices.reduce((a, b) => a + b, 0) / prices.length).toLocaleString("en-US", { style: "currency", currency: "USD" }) : "$0";
  
    // Update insights in HTML
    document.getElementById("highest-price").querySelector("b").textContent = highestSoldPrice;
    document.getElementById("total-sales").querySelector("b").textContent = `${totalSales} Units`;
    document.getElementById("average-price").querySelector("b").textContent = averagePrice;
  }
  