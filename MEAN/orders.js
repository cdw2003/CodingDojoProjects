function orderSupplies(item, callback) {
  let warehouse; //undefined
  const deliveryTime = Math.random() * 3000;

  setTimeout(function(){
    warehouse = {
      paint: {
        product: 'Neon Green Paint',
        directions: function() { return 'mix it!' }
      },
      brush: {
        product: 'Horsehair brush',
        directions: function() { return 'start painting!' }
      }
    };

    callback(warehouse[item]);
  }, deliveryTime);
}

orderSupplies('brush', receivedItem);

let items=[];

function receivedItem(item){
  let count=0;
  items.push(item);
  console.log(items);
  for(let i=0; i<items.length; i++){
    if(items[i].product == 'Neon Green Paint'){
      count +=1;
    }
  }
  if(count > 0){
    console.log(`Received ${ item.product }, time to ${ item.directions()}`);
  }
  else{
    console.log("You must purchase paint before you can start painting.");
  }
}

orderSupplies('paint', receivedItem);
