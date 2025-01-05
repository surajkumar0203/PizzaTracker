let order_ref = document.querySelector("#order-id");
let order_id = order_ref.innerText.split(":")[1].trim()



// Create WebSocket connection.
const socket = new WebSocket(`ws://127.0.0.1:8000/ws/pizza/${order_id}/`);

socket.onopen = (event) =>{
    console.log('Connected to WebSocket server.');
}
// on receiving message
socket.onmessage = (event) => {
    const data= JSON.parse(event.data);
    
    let progress_percentage=data.payload.progress_percentage
    let status=data.payload.status
    
    changeInUI(progress_percentage,status)
}


socket.onerror = (error) => {
    console.error('WebSocket error:', error);
}

const changeInUI = (progress_percentage,status) => {
    const progress_barRef=document.querySelector('.progress-bar')
    const show_order_statusRef=document.querySelector('#show_order_status')
    show_order_statusRef.innerText = status
    if(progress_percentage===100){
        progress_barRef.classList.add('bg-success')
    }
    progress_barRef.style.width = `${progress_percentage}%`
    progress_barRef.innerText = `${progress_percentage}%`

}