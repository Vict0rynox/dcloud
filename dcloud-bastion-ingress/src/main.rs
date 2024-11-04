
async fn say_hello() {
    println!("world!");
}


#[tokio::main]
async fn main() {
    let op = say_hello();
    print!("Hello ");
    op.await;
}
