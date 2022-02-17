// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;
pragma experimental ABIEncoderV2;

// struct RelationshipIDToPattern{ string ind_pat_val; } string key = _ind_id - value = the structure. mapping id to pattern - can retrieve data using the id 
// mapping (string => RelationshipIDToPattern) contentIDs;
contract RelationshipStorage {
    
    string[] public relationshipIDs;
    string[] public contentIDs;

    struct RelationshipID{
        string stixID;
        string srcID;
        string relType;
        string trgtID;
    }
    struct DataLocation{
        string contentID;
        string stixID;    
    }
    
    //QUERY THE DATA   string key = src, value = trgtID  
    mapping (string => RelationshipID) relationship_list;
     
    //TIE THE ID TO THE CONTENT address mal_id - value = contentID. 
    mapping(string=> DataLocation) data_locations;
    
    
    function setRelationship(string memory _contentID, string memory _stixID, string memory _srcID) public {
        RelationshipID storage relationship = relationship_list[_srcID];
        relationship.stixID= _stixID;
        relationship.srcID = _srcID;
        relationshipIDs.push(_stixID);
            
        DataLocation storage content = data_locations[_stixID];       
        content.contentID= _contentID;
        content.stixID = _stixID;
        contentIDs.push(_contentID);
    }
      
  function getContentIDs() view public returns(string[] memory){
      return contentIDs;
  }         
  
  function getRelationships() view public returns(string[] memory){
      return relationshipIDs;
  }
  
  function getContentID(string memory _stixID) view public returns(string memory){
      return data_locations[_stixID].contentID;
  }         
  
  function getRelationship(string memory _srcID) view public returns (string memory){
      return relationship_list[_srcID].stixID;

  }



}