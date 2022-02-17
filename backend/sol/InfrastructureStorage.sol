// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;
pragma experimental ABIEncoderV2;

// struct InfrastructureIDToPattern{ string ind_pat_val; } string key = _ind_id - value = the structure. mapping id to pattern - can retrieve data using the id 
// mapping (string => InfrastructureIDToPattern) contentIDs;
contract InfrastructureStorage {
    
    string[] public infrastructureIDs;
    string[] public contentIDs;

    struct InfrastructureID{
        string stixID;
        string infra_name;
    }
    struct DataLocation{
        string contentID;
        string stixID;    
    }
    
    //QUERY THE DATA   string key = infrastructure, ID (ipv4,file hash, url etc) value = Infrastructure for that pattern.  
    mapping (string => InfrastructureID) infrastructure_list;
     
    //TIE THE ID TO THE CONTENT address ind_id - value = contentID. 
    mapping(string=> DataLocation) data_locations;
    
    
    function setInfrastructure(string memory _contentID, string memory _stixID, string memory _infra_name) public {
        InfrastructureID storage infrastructure = infrastructure_list[_infra_name];
        infrastructure.stixID= _stixID;
        infrastructure.infra_name = _infra_name;
        infrastructureIDs.push(_stixID);
            
        DataLocation storage content = data_locations[_stixID];       
        content.contentID= _contentID;
        content.stixID = _stixID;
        contentIDs.push(_contentID);
    }
      
  function getContentIDs() view public returns(string[] memory){
      return contentIDs;
  }         
  
  function getInfrastructures() view public returns(string[] memory){
      return infrastructureIDs;
  }
  
  function getContentID(string memory _stixID) view public returns(string memory){
      return data_locations[_stixID].contentID;
  }         
  
  function getInfrastructure(string memory _infra_name) view public returns (string memory){
      return infrastructure_list[_infra_name].stixID;

  }



}