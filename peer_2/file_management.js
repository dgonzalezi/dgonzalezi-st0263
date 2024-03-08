const express = require('express');
const readline = require('readline');
const servidor = express();
const puertoServidor = 3000;

servidor.use(express.json());

// Ruta para la selección de archivos
servidor.post('/seleccionar_archivos', (req, res) => {
    const listaArchivos = req.body.listaArchivos;
    const indicesElegidos = req.body.indicesElegidos;

    const archivosSeleccionados = indicesElegidos.map(indice => parseInt(indice, 10) - 1)
                                                  .filter(indice => indice >= 0 && indice < listaArchivos.length)
                                                  .map(indice => listaArchivos[indice]);

    console.log("Lista de archivos seleccionados:", archivosSeleccionados);

    res.json({ archivosSeleccionados });
});

servidor.listen(puertoServidor, () => {
    console.log(`Servidor de archivos funcionando en puerto ${puertoServidor}`);
});

// Desarrollado por David González Idárraga
