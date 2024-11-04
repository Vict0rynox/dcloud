use tokio::io::AsyncReadExt;
use tokio::net::{TcpListener, TcpStream};


/// Receive connection from local machine
/// Receive connections from kuber cluster (? one port for all, and routing by virtual service)  
/// Proxy all request from kuber cluster to local machine 
/// 
/// 

#[tokio::main]
async fn main() {
    let listener = TcpListener::bind("127.0.0.1:8080").await.unwrap();
    loop {
        let (socket, _) = listener.accept().await.unwrap();
        process(socket).await;
    }
}

async fn process(socket: TcpStream) {
    
}
