// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;
pragma experimental ABIEncoderV2;

// struct AttackPatternIDToPattern{ string att_pat_val; } string key = _ind_id - value = the structure. mapping id to pattern - can retrieve data using the id 
// mapping (string => AttackPatternIDToPattern) contentIDs;
contract AttackPatternStorage {
    
    string[] public attack_patternIDs;
    string[] public contentIDs;

    struct AttackPatternID{
        string stixID;
        string att_pat_val;
    }
    struct DataLocation{
        string contentID;
        string stixID;    
    }
    
    //QUERY THE DATA   string key = attack_pattern, ID (ipv4,file hash, url etc) value = AttackPattern for that pattern.  
    mapping (string => AttackPatternID) attack_pattern_list;
     
    //TIE THE ID TO THE CONTENT address ind_id - value = contentID. 
    mapping(string=> DataLocation) data_locations;
    
    
    function setAttackPattern(string memory _contentID, string memory _stixID, string memory _att_pat_val) public {
        AttackPatternID storage attack_pattern = attack_pattern_list[_att_pat_val];
        attack_pattern.stixID= _stixID;
        attack_pattern.att_pat_val = _att_pat_val;
        attack_patternIDs.push(_stixID);
            
        DataLocation storage content = data_locations[_stixID];       
        content.contentID= _contentID;
        content.stixID = _stixID;
        contentIDs.push(_contentID);
    }
      
  function getContentIDs() view public returns(string[] memory){
      return contentIDs;
  }         
  
  function getAttackPatterns() view public returns(string[] memory){
      return attack_patternIDs;
  }
  
  function getContentID(string memory _stixID) view public returns(string memory){
      return data_locations[_stixID].contentID;
  }         
  
  function getAttackPattern(string memory _att_pat_val) view public returns (string memory){
      return attack_pattern_list[_att_pat_val].stixID;

  }



}