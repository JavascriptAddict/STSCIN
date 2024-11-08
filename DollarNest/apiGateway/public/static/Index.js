// Replace 'YOUR_MAPBOX_dataESS_TOKEN' with your actual Mapbox token 
mapboxgl.accessToken = "[INSERT MAPBOX API KEY HERE]";
 
const map = new mapboxgl.Map({ 
  container: 'map', // ID of the container element 
  style: 'mapbox://styles/mapbox/streets-v11', // Map style 
  center: [100.3087117620608, 5.377901215366127], // Coordinates for Penang, Malaysia 
  zoom: 16, // Initial zoom level suitable for city view 
  pitch: 35, // Angle for a 30-degree tilt 
  bearing: -10, // Adjust to control the map rotation 
  antialias: true // Enables better 3D rendering quality 
}); 

map.on('load', () => { 
  // Sample GeoJSON data representing different areas with a hotness score 
  const geojsonData = { 
    "type": "FeatureCollection", 
    "features": [ 
    // Green Zone 
    // Green Building 1 
      { 
        "type": "Feature", 
        "properties": { "hotness": 0.1 }, // Lower "hotness" value 
        "geometry": { 
          "type": "Polygon", 
          "coordinates": [[[100.30488669552525, 5.377310413484559],[100.30587019348282, 5.377375691463578],[100.30570627715657, 5.3769550110315425],[100.30559699960571, 5.376715658242187],[100.3056188551159, 5.376414653843179],[100.30498140273598, 5.376334869519699],[100.30488669552525, 5.377310413484559]]] 
        } 
      }, 
      { 
        "type": "Feature", 
        "properties": { "hotness": 0.1 }, // Lower "hotness" value 
        "geometry": { 
          "type": "Polygon", 
          "coordinates": [[[100.30560272881905, 5.379822789188085], [100.30614054921276, 5.379793805550271], [100.30579644882803, 5.380362495811838], [100.30542482041255, 5.380622859850567], [100.30513233508555, 5.380663969951761], [100.30493619786624, 5.380646840743264], [100.3048157627316, 5.380609156482896], [100.30461618450846, 5.3805029553729], [100.3042755251276, 5.380242591282836], [100.30447166234688, 5.379978801235868], [100.30496716690088, 5.380252868814833], [100.30526653423559, 5.3802049069974185], [100.30545578944718, 5.380074724902542], [100.30555557855874, 5.379913710167717], [100.30560272881905, 5.379822789188085]]] 
        } 
      }, 
      { 
        "type": "Feature", 
        "properties": { "hotness": 0.1 }, // Lower "hotness" value 
        "geometry": { 
          "type": "Polygon", 
          "coordinates": [[[100.30488669552525, 5.377310413484559],[100.30587019348282, 5.377375691463578],[100.30570627715657, 5.3769550110315425],[100.30559699960571, 5.376715658242187],[100.3056188551159, 5.376414653843179],[100.30498140273598, 5.376334869519699],[100.30488669552525, 5.377310413484559]]] 
        } 
      }, 
      { 
        "type": "Feature", 
        "properties": { "hotness": 0.1 }, // Lower "hotness" value 
        "geometry": { 
          "type": "Polygon", 
          "coordinates": [[[100.30620526307587, 5.378879640621196],[100.30628391583599, 5.3796120355185275],[100.3064180881915, 5.379902229479262],[100.30662166004123, 5.3800127795231445],[100.3069223911829, 5.379911441983682],[100.30693627108174, 5.37903625344063],[100.30658927361061, 5.378911884440252],[100.30620526307587, 5.378879640621196]]] 
        } 
      }, 
      { 
        "type": "Feature", 
        "properties": { "hotness": 0.3 }, // Lower "hotness" value 
        "geometry": { 
          "type": "Polygon", 
          "coordinates": [[[100.31410071539929, 5.376992688347804], [100.31505558178705, 5.376875190456251], [100.31466934369762, 5.375892479929811], [100.3137989567199, 5.376205845924842], [100.31410071539929, 5.376992688347804]]] 
        } 
      }, 
      

    //   RED ZONES 
    // orange building 1 
      { 
        "type": "Feature", 
        "properties": { "hotness": 0.8 }, // Higher "hotness" value 
        "geometry": { 
          "type": "Polygon", 
          "coordinates": [[[100.3095477615688, 5.3800301984681], [100.30988696990202, 5.381274406748107], [100.31169012998923, 5.38175431497599], [100.31208289753297, 5.381594345608767],[100.3117079830594, 5.380136844991804], [100.3095477615688, 5.3800301984681]]] 
        } 
      }, 
      { 
        "type": "Feature", 
        "properties": { "hotness": 0.8 }, // Higher "hotness" value 
        "geometry": { 
          "type": "Polygon", 
          "coordinates": [[[100.30685739985913, 5.376974923484296], [100.30715780725428, 5.376932196981983], [100.30738311280646, 5.375970849834735], [100.30710416307518, 5.375981531478049], [100.30643897525451, 5.376633111365523], [100.30665355197085, 5.37710310298256], [100.30685739985913, 5.376974923484296]]] 
        } 
      }, 
      { 
        "type": "Feature", 
        "properties": { "hotness": 0.7 }, // Higher "hotness" value 
        "geometry": { 
          "type": "Polygon", 
          "coordinates": [[[100.3085128655943, 5.380213689786726], [100.30872744231065, 5.380640952394182], [100.30945703309129, 5.380363236554677], [100.30940338891222, 5.380000063191677], [100.3085128655943, 5.380213689786726]]] 
        } 
      }, 
      { 
        "type": "Feature", 
        "properties": { "hotness": 0.8 }, // Higher "hotness" value 
        "geometry": { 
          "type": "Polygon", 
          "coordinates": [[[100.3085128655943, 5.380213689786726], [100.30872744231065, 5.380640952394182], [100.30945703309129, 5.380363236554677], [100.30940338891222, 5.380000063191677], [100.3085128655943, 5.380213689786726]]] 
        } 
      }, 
    // Red Building 1 
      { 
        "type": "Feature", 
        "properties": { "hotness": 0.9 }, // Higher "hotness" value 
        "geometry": { 
          "type": "Polygon", 
          "coordinates": [[[100.30567320028676, 5.378939521982876],[100.30580274600932, 5.379165228658221],[100.30581662590816, 5.379727191853499],[100.30612661031572, 5.379694948077647],[100.30618675654405, 5.379616641757736],[100.30613123694866, 5.378962553280121],[100.30595542489665, 5.378713815239034],[100.30567320028676, 5.378939521982876],]] 
        } 
      } 
      // Add more areas as needed 
    ] 
  };  

  // Add the GeoJSON data as a source 
  map.addSource('areas', { 
    "type": "geojson", 
    "data": geojsonData 
  }); 

  // Add a fill layer with a color gradient based on the "hotness" property 
  map.addLayer({ 
    'id': 'area-heatmap', 
    'type': 'fill', 
    'source': 'areas', 
    'paint': {'fill-color': [ 
            'interpolate', 
            ['linear'], 
            ['get', 'hotness'], // Get the "hotness" property 
            0, '#00ff00', // Green for low interest 
            0.5, '#ffff00', // Yellow for medium interest 
            1, '#ff0000'  // Red for high interest 
          ], 
          'fill-opacity': 0.6 
        } 
      }); 
       
      // Add a 3D layer for buildings if needed 
      map.addLayer({ 
        'id': '3d-buildings', 
        'source': 'composite', 
        'source-layer': 'building', 
        'filter': ['==', 'extrude', 'true'], 
        'type': 'fill-extrusion', 
        'minzoom': 15, 
        'paint': { 
          'fill-extrusion-color': '#aaa', 
          'fill-extrusion-height': [ 
            'interpolate', ['linear'], ['zoom'], 
            15, 0, 
            16.05, ['get', 'height'] 
          ], 
          'fill-extrusion-base': [ 
            'interpolate', ['linear'], ['zoom'], 
            15, 0, 
            16.05, ['get', 'min_height'] 
          ], 
          'fill-extrusion-opacity': 0.6 
        } 
      }); 
    });

// For trending table text color change
// Function to update percentage text color based on positive or negative value
function updatePercentageColors() {
  // Select all cells in the last column of the Hotspots table
  const percentageCells = document.querySelectorAll('#trending tbody tr td:last-child');

  percentageCells.forEach(cell => {
    const value = parseFloat(cell.textContent);
    
    // Apply color based on value
    if (value > 0) {
      cell.classList.add('green-text');
      cell.classList.remove('red-text');
    } else if (value < 0) {
      cell.classList.add('red-text');
      cell.classList.remove('green-text');
    } else {
      cell.classList.remove('green-text', 'red-text');
    }
  });
}

// Run the function after the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', updatePercentageColors);

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

function analyzeTopAreas(estates) {
  if (!estates || estates.length === 0) return [];

  // Sort estates by transactionDate (assuming format is DD/MM/YYYY)
  estates.sort((a, b) => {
    const dateA = a.transactionDate.split("/").reverse().join("");
    const dateB = b.transactionDate.split("/").reverse().join("");
    return dateA.localeCompare(dateB);
  });

  // Count occurrences of each area
  const areaCount = {};
  estates.forEach((estate) => {
    areaCount[estate.area] = (areaCount[estate.area] || 0) + 1;
  });

  // Get top 10 trending areas based on count
  const topAreas = Object.entries(areaCount)
    .sort((a, b) => b[1] - a[1]) // Sort areas by frequency
    .slice(0, 10) // Get top 10 areas
    .map(item => item[0]); // Extract area names only

  // Calculate average price and percentage gain/loss for each top area
  const topAreaAnalysis = topAreas.map((area) => {
    // Filter estates for the current area
    const areaEstates = estates.filter(estate => estate.area === area);

    // Calculate average price for the area
    const totalAreaPrice = areaEstates.reduce((sum, estate) => sum + estate.price, 0);
    const averagePrice = totalAreaPrice / areaEstates.length;

    // Calculate percentage gain/loss
    const firstPrice = areaEstates[0].price;
    const lastPrice = areaEstates[areaEstates.length - 1].price;
    const percentageGainLoss = ((lastPrice - firstPrice) / firstPrice) * 100;

    return {
      area: area,
      averagePrice: averagePrice.toFixed(2),
      percentageGainLoss: percentageGainLoss.toFixed(2) + "%"
    };
  });

  return topAreaAnalysis;
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
          // Handle data here
          analyzedData = analyzeTopAreas(data);
          html = "";
          console.log(analyzedData)
          var hotspotDiv = document.getElementById("hotspotDiv");
          for(var count=0; count < analyzedData.length; count++){
            html += `<tr>
                      <td>${analyzedData[count].area}</td>
                      <td>${analyzedData[count].averagePrice}</td>
                      <td>${analyzedData[count].percentageGainLoss}</td>
                    </tr>`
          }
          hotspotDiv.innerHTML = html;
          updatePercentageColors();
      } else {
          console.log("No data found.");
      }
  });
});