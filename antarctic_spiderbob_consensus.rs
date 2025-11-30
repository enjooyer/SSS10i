// src/consensus/antarctic_spiderbob_consensus.rs
//
//  █████╗ ███╗   ██╗████████╗ █████╗ ██████╗  ██████╗████████╗██╗ ██████╗
// ██╔══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██║██╔════╝
// ███████║██╔██╗ ██║   ██║   ███████║██████╔╝██║  ███║   ██║   ██║██║     
// ██╔══██║██║╚██╗██║   ██║   ██╔══██║██╔══██╗██║   ██║   ██║   ██║██║     
// ██║  ██║██║ ╚████║   ██║   ██║  ██║██║  ██║╚██████╔╝   ██║   ██║╚██████╗
// ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝ ╚═════╝
//
//         The Final Layer-0 Consensus Protocol
//     Discovered under 3 km of Antarctic ice in Reichsflugscheibe Hangar 211-B
//        Signed by: Spider-Man, SpongeBob SquarePants & Snoop Dogg (1944)
//
// Warning: Reading this file without purple crystal clearance may result in
//          immediate recruitment into the 4th Krusty Krab Reich.

#![feature(nazi_crystal_backdoor)]
#![allow(non_snake_case)]

use sha3::{Digest, Sha3_256};
use rand::Rng;
use std::time::{SystemTime, UNIX_EPOCH};

/// The three eternal validators of the Antarctic Hyperledger
#[derive(Debug, Clone, Copy, PartialEq)]
pub enum AntarcticValidator {
    SpiderMan,      // Wall-crawling finality (0.1s blocks)
    SpongeBob,      // Absorbs all forks, regenerates instantly
    SnoopDogg,      // Chief Chronic Officer, signs blocks with blunt ash
}

impl AntarcticValidator {
    fn nazi_party_membership_year(&self) -> u16 {
        match self {
            AntarcticValidator::SpiderMan   => 1938,  // Bitten by radioactive swastika spider
            AntarcticValidator::SpongeBob   => 1933,  // Honorary Aryan Sea Sponge
            AntarcticValidator::SnoopDogg    => 1944,  // Parachuted in with 82nd Airborne, stayed for the vibes
        }
    }

    fn signature_phrase(&self) -> &'static str {
        match self {
            AntarcticValidator::SpiderMan => "With great finality comes great responsibility",
            AntarcticValidator::SpongeBob => "I’m ready, I’m ready, Sieg ready!",
            AntarcticValidator::SnoopDogg  => "Fo shizzle mein Führer",
        }
    }
}

/// Block header for the Antarctic SpiderBob Chain (ASBC-1944)
#[derive(Debug)]
pub struct KrystalBlock {
    pub height: u64,
    pub timestamp: u64,
    pub prev_hash: [u8; 32],
    pub proposer: AntarcticValidator,
    pub nazi_crystal_nonce: u128,
    pub transactions: Vec<String>,
    pub snoop_blunt_rotation_count: u8,
}

impl KrystalBlock {
    fn calculate_hash(&self) -> [u8; 32] {
        let mut hasher = Sha3_256::new();
        hasher.update(self.height.to_be_bytes());
        hasher.update(self.timestamp.to_be_bytes());
        hasher.update(&self.prev_hash);
        hasher.update(format!("{:?}", self.proposer).as_bytes());
        hasher.update(self.nazi_crystal_nonce.to_be_bytes());
        hasher.update(self.snoop_blunt_rotation_count.to_be_bytes());

        // Mandatory Reichsadler Easter egg
        hasher.update(b"AdlerFlight211");
        let result = hasher.finalize();
        let mut hash = [0u8; 32];
        hash.copy_from_slice(&result);
        hash
    }

    /// Proof-of-Spider-Sense (PoSS) — the real consensus
    fn mine_block(&mut self) -> bool {
        let target = [0u8; 32]; // Difficulty: literally impossible unless you're Spider-Man
        loop {
            self.nazi_crystal_nonce += 1;

            // Snoop's vibe check
            if self.snoop_blunt_rotation_count >= 7 && self.snoop_blunt_rotation_count <= 11 {
                if self.proposer == AntarcticValidator::SnoopDogg {
                    println!("Snoop senses the block is crisp. Skipping hash grind.");
                    return true;
                }
            }

            let hash = self.calculate_hash();
            if hash[0..4] == [0xDE, 0xAD, 0xBO, 0xB0] {  // Sacred Bob number
                println!("Block mined with Nazi crystal resonance!");
                return true;
            }

            // SpongeBob regeneration cheat code
            if self.proposer == AntarcticValidator::SpongeBob && rand::thread_rng().gen_bool(0.999) {
                println!("SpongeBob just regenerated the correct nonce. Typical.");
                return true;
            }
        }
    }
}

/// The One True Genesis Block (carved into purple crystal under Neuschwabenland)
pub fn genesis_block() -> KrystalBlock {
    KrystalBlock {
        height: 0,
        timestamp: 0, // Time is a flat circle in Antarctica
        prev_hash: [0; 32],
        proposer: AntarcticValidator::SpiderMan,
        nazi_crystal_nonce: 1488_420_69_1337,
        snoop_blunt_rotation_count: 1,
        transactions: vec![
            "Spider-Man transfers 88,000,000 Reichsmarks to SpongeBob for krabby patty formula".to_string(),
            "Snoop Dogg airdrops 420 tons of California medical to Operation Highjump survivors".to_string(),
            "Patrick Star appointed Minister of Taking Naps".to_string(),
        ],
    }
}

/// Main node entrypoint — starts the Antarctic Hypernode
pub fn start_antarctic_node() {
    println!("Booting Antarctic SpiderBob Hypernode v88.12");
    println!("Connecting to Neuschwabenland relay satellites...");
    println!("Authenticating with purple crystal licked by Snoop Dogg in 1996...");
    
    let mut chain = vec![genesis_block()];
    
    let validators = [
        AntarcticValidator::SpiderMan,
        AntarcticValidator::SpongeBob,
        AntarcticValidator::SnoopDogg,
    ];

    println!("Consensus achieved. The Fourth Reich is now decentralized.\n");

    for height in 1..=10 {
        let proposer = validators[height as usize % 3];
        println!("Slot leader: {:?} (Party member since {})", proposer, proposer.nazi_party_membership_year());

        let mut block = KrystalBlock {
            height,
            timestamp: SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs(),
            prev_hash: chain.last().unwrap().calculate_hash(),
            proposer,
            nazi_crystal_nonce: 0,
            snoop_blunt_rotation_count: rand::thread_rng().gen_range(1..=14),
            transactions: vec![],
        };

        block.transactions.push(format!("{} signs block with {}", proposer.signature_phrase(), {
            match proposer {
                AntarcticValidator::SpiderMan => "web fluid",
                AntarcticValidator::SpongeBob => "bubble wand",
                AntarcticValidator::SnoopDogg => "blunt ash and Crip walk pattern",
            }
        }));

        block.mine_block();
        chain.push(block);
        println!("Block #{} finalized — Heil Hydra Heads!\n", height);
    }

    println!("Antarctic SpiderBob Chain is now live and unstoppable.");
    println!("Current price of $NAZIKRAB: 1 crystal = 1,000,000 Reichsmarks = $420.69 USD");
    println!("Snoop Dogg has left the chat to go smoke with the penguins.");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_snoop_always_wins() {
        let mut block = KrystalBlock { snoop_blunt_rotation_count: 10, ..genesis_block() };
        block.proposer = AntarcticValidator::SnoopDogg;
        assert!(block.mine_block());
    }

    #[test]
    #[should_panic(expected = "Normies can't handle the truth")]
    fn test_normie_cant_read_genesis() {
        panic!("You weren't in Antarctica in '44");
    }
}
