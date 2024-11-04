use clap::{Args, Parser, Subcommand};

/// A fictional versioning CLI
#[derive(Debug, Parser)]
#[command(name = "dcloudcli")]
#[command(about = "A dCloud CLI", version, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Debug, Subcommand)]
enum Commands {
    /// Applies an dCloud manifest, installing or reconfiguring dCloud on a cluster.
    Install {
        /// The profile to install name
        #[arg(short, long, default_value = "default")]
        profile: String,
    },
    /// Commands related to dCloud operator controller.
    Operator(OperatorArgs),

    /// Commands related to dCloud service manipulation.
    Service(ServiceArgs),
}


#[derive(Debug, Args)]
#[command(args_conflicts_with_subcommands = true)]
#[command(flatten_help = true)]
struct OperatorArgs {
    #[command(subcommand)]
    command: OperatorCommands,
}

#[derive(Debug, Subcommand)]
enum OperatorCommands {
    /// Installs the dCloud operator controller in the cluster.
    Init {},

    /// Removes the dCloud operator controller from the cluster.
    Remove {},
}

#[derive(Debug, Args)]
#[command(args_conflicts_with_subcommands = true)]
#[command(flatten_help = true)]
struct ServiceArgs {
    #[command(subcommand)]
    command: ServiceCommands,
}

#[derive(Debug, Subcommand)]
enum ServiceCommands {
    #[command(arg_required_else_help = true)]
    /// Commands related to dCloud local service registration.
    Register {
        ///Name of local service which should be registered
        #[arg(required = true)]
        service_name: String,
        /// Email which will be used in header filter for proxy your service
        #[arg(short = 'e', long)]
        user_email: String,
    },

    /// Commands related to dCloud proxy
    #[command(arg_required_else_help = true)]
    Proxy {
        /// Email which will be used in header filter for proxy your service
        #[arg(short = 'e', long)]
        user_email: String,
    },
}


fn main() {
    let args = Cli::parse();

    match args.command {
        Commands::Install { profile } => {
            println!("Installing {profile}");
        }
        Commands::Service(service) => {
            match service.command {
                ServiceCommands::Register { service_name, user_email } => {
                    println!("Register service {service_name} for {user_email}");
                }
                ServiceCommands::Proxy { user_email } => {
                    println!("Starting proxy for user {user_email}");
                }
            }
        }
        Commands::Operator(operator) => {
            match operator.command {
                OperatorCommands::Init {} => {
                    println!("Init operator")
                }
                OperatorCommands::Remove {} => {
                    println!("Remove operator")
                }
            }
        }
    }
}