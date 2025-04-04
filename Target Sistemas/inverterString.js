const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  function inverterString(str) {
      let inverted = '';
      for (let i = str.length - 1; i >= 0; i--) {
          inverted += str[i];
      }
      return inverted;
  }
  
  readline.question('Digite uma string para inverter: ', (texto) => {
      console.log('String invertida:', inverterString(texto));
      readline.close();
  });