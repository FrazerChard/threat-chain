// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;
pragma experimental ABIEncoderV2;

// struct IndicatorIDToPattern{ string ind_pat_val; } string key = _ind_id - value = the structure. mapping id to pattern - can retrieve data using the id 
// mapping (string => IndicatorIDToPattern) contentIDs;
contract IndicatorStorage {
    
    string[] public indicatorIDs;
    string[] public contentIDs;

    struct IndicatorID{
        string stixID;
        string ind_pat_val;
    }
    struct DataLocation{
        string contentID;
        string stixID;    
    }
    
    //QUERY THE DATA   string key = indicator, ID (ipv4,file hash, url etc) value = Indicator for that pattern.  
    mapping (string => IndicatorID) indicator_list;
     
    //TIE THE ID TO THE CONTENT address ind_id - value = contentID. 
    mapping(string=> DataLocation) data_locations;
    
    
    function setIndicator(string memory _contentID, string memory _stixID, string memory _ind_pat_val) public {
        IndicatorID storage indicator = indicator_list[_ind_pat_val];
        indicator.stixID= _stixID;
        indicator.ind_pat_val = _ind_pat_val;
        indicatorIDs.push(_stixID);
            
        DataLocation storage content = data_locations[_stixID];       
        content.contentID= _contentID;
        content.stixID = _stixID;
        contentIDs.push(_contentID);
    }
      
  function getContentIDs() view public returns(string[] memory){
      return contentIDs;
  }         
  
  function getIndicators() view public returns(string[] memory){
      return indicatorIDs;
  }
  
  function getContentID(string memory _stixID) view public returns(string memory){
      return data_locations[_stixID].contentID;
  }         
  
  function getIndicator(string memory _ind_pat_val) view public returns (string memory){
      return indicator_list[_ind_pat_val].stixID;

  }



}