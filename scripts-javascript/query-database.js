import pg from 'pg'
const { Client } = pg


async function queryDatabase() {
    const client = new Client({
        user: 'postgres',
        host: 'localhost',
        database: 'NOME DO BANCO DE DADOS',
        password:'SENHA',
        port:5432,
    });

    await client.connect();

    await client.query('SELECT * FROM inputs', (err, res) => {
        if (err) throw err;
        console.log("CONSOLE LOG DA AWAIT CLIENT QUERY",res.rows);
        client.end();
    });
}

queryDatabase();


