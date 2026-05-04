const API_URL = "http://127.0.0.1:8000";

async function add_usuario(){
    const id = document.getElementById("id").value;
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
    const retorno = document.getElementById("retorno-api");

    const response = await fetch(`${API_URL}/criar-usuario`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id: Number(id),
            nome: nome,
            email: email,
            senha: senha
        })
    });

    const data = await response.json();
    console.log(data);

    if (data.erro){
        retorno.innerHTML=`<br>${data.erro}`;
    } else {
        retorno.innerHTML=`<br>Usuário ${id} adicionado com sucesso.`;
        setTimeout(() => {window.location.reload();}, 3000);
    }
    
}