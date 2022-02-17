// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;
pragma experimental ABIEncoderV2;

// struct IntrusionSetIDToPattern{ string ind_pat_val; } string key = _ind_id - value = the structure. mapping id to pattern - can retrieve data using the id 
// mapping (string => IntrusionSetIDToPattern) contentIDs;
contract IntrusionSetStorage {
    
    string[] public intrusion_setIDs;
    string[] public contentIDs;

    struct IntrusionSetID{
        string stixID;
        string itset_name;
    }
    struct DataLocation{
        string contentID;
        string stixID;    
    }
    
    //QUERY THE DATA   string key = intrusion_set, ID (ipv4,file hash, url etc) value = IntrusionSet for that pattern.  
    mapping (string => IntrusionSetID) intrusion_set_list;
     
    //TIE THE ID TO THE CONTENT address ind_id - value = contentID. 
    mapping(string=> DataLocation) data_locations;
    
    
    function setIntrusionSet(string memory _contentID, string memory _stixID, string memory _itset_name) public {
        IntrusionSetID storage intrusion_set = intrusion_set_list[_itset_name];
        intrusion_set.stixID= _stixID;
        intrusion_set.itset_name = _itset_name;
        intrusion_setIDs.push(_stixID);
            
        DataLocation storage content = data_locations[_stixID];       
        content.contentID= _contentID;
        content.stixID = _stixID;
        contentIDs.push(_contentID);
    }
      
  function getContentIDs() view public returns(string[] memory){
      return contentIDs;
  }         
  
  function getIntrusionSets() view public returns(string[] memory){
      return intrusion_setIDs;
  }
  
  function getContentID(string memory _stixID) view public returns(string memory){
      return data_locations[_stixID].contentID;
  }         
  
  function getIntrusionSet(string memory _itset_name) view public returns (string memory){
      return intrusion_set_list[_itset_name].stixID;

  }



}