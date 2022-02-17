// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;
pragma experimental ABIEncoderV2;

// struct ThreatActorIDToPattern{ string ind_pat_val; } string key = _ind_id - value = the structure. mapping id to pattern - can retrieve data using the id 
// mapping (string => ThreatActorIDToPattern) contentIDs;
contract ThreatActorStorage {
    
    string[] public threat_actorIDs;
    string[] public contentIDs;

    struct ThreatActorID{
        string stixID;
        string ta_name;
    }
    struct DataLocation{
        string contentID;
        string stixID;    
    }
    
    //QUERY THE DATA   string key = threat_actor, ID (ipv4,file hash, url etc) value = ThreatActor for that pattern.  
    mapping (string => ThreatActorID) threat_actor_list;
     
    //TIE THE ID TO THE CONTENT address ind_id - value = contentID. 
    mapping(string=> DataLocation) data_locations;
    
    
    function setThreatActor(string memory _contentID, string memory _stixID, string memory _ta_name) public {
        ThreatActorID storage threat_actor = threat_actor_list[_ta_name];
        threat_actor.stixID= _stixID;
        threat_actor.ta_name = _ta_name;
        threat_actorIDs.push(_stixID);
            
        DataLocation storage content = data_locations[_stixID];       
        content.contentID= _contentID;
        content.stixID = _stixID;
        contentIDs.push(_contentID);
    }
      
  function getContentIDs() view public returns(string[] memory){
      return contentIDs;
  }         
  
  function getThreatActors() view public returns(string[] memory){
      return threat_actorIDs;
  }
  
  function getContentID(string memory _stixID) view public returns(string memory){
      return data_locations[_stixID].contentID;
  }         
  
  function getThreatActor(string memory _ta_name) view public returns (string memory){
      return threat_actor_list[_ta_name].stixID;

  }



}